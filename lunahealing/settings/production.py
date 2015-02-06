from lunahealing.settings.common import *

import dj_database_url
import os

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': dj_database_url.config()
}

# Static asset configuration
STATIC_ROOT = 'staticfiles'
STATICFILES_DIRS = (
    os.path.join(APP_PATH, 'static'),
)

MEDIA_ROOT = 'media'

ALLOWED_HOSTS = ['lunahealing.herokuapp.com', 'www.lunahealing.ca']

INSTALLED_APPS.extend([
    'gunicorn',
])
