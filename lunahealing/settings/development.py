from lunahealing.settings.common import *

import os

HOME_DIR = os.path.expanduser("~")

SECRET_KEY = ')7b)xf5r($em5_h%=bnsomcb)40118-lj))!dxlyk3^uzj8bv3'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'lunahealing',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        }
}

STATIC_ROOT = '/tmp/static'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

MEDIA_ROOT = '/tmp/media'

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = '%s/Development/Django/lunahealing/emails' % HOME_DIR

TEST_RUNNER = 'django.test.runner.DiscoverRunner'
