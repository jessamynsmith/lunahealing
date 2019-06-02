#!/bin/bash

# This script will quit on the first error that is encountered.
set -e

CIRCLE=$1

DEPLOY_DATE=`date "+%FT%T%z"`
SECRET=$(openssl rand -base64 58 | tr '\n' '_')

heroku config:set --app=lunahealing \
NEW_RELIC_APP_NAME='lunahealing' \
ADMIN_EMAIL="jessamyn@lunahealing.ca" \
ADMIN_NAME="lunahealing" \
DJANGO_SETTINGS_MODULE=lunahealing.settings.production \
DJANGO_SECRET_KEY="$SECRET" \
DEPLOY_DATE="$DEPLOY_DATE" \
> /dev/null

if [ $CIRCLE ]
then
    git push https://heroku:$HEROKU_API_KEY@git.heroku.com/lunahealing.git master
else
    git push heroku master
fi

heroku run python manage.py syncdb --noinput --app=lunahealing
heroku run python manage.py migrate --noinput --app=lunahealing
