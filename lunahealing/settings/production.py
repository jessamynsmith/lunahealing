from lunahealing.settings.common import *

import dj_database_url
import os

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Parse database configuration from $DATABASE_URL
DATABASES = {
    'default': dj_database_url.config()
}

# Static asset configuration
STATIC_ROOT = 'staticfiles'

MEDIA_ROOT = 'media'

ALLOWED_HOSTS = ['lunahealing.herokuapp.com', 'www.lunahealing.ca']

INSTALLED_APPS.extend([
    'gunicorn',
])
