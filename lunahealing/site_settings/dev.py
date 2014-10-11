from lunahealing.site_settings.common import *

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

MEDIA_ROOT = '/tmp/media'
MEDIA_URL = ''

STATIC_ROOT = '/tmp/static'
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = '%s/Development/Django/lunahealing/emails' % HOME_DIR

INSTALLED_APPS.extend([
    'django_nose',
])

# Use nose to run all tests
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--cover-branches',
    '--cover-package=lunahealing',
    '--cover-inclusive',  # Cover all files
    '--cover-html',
    '--cover-html-dir=%s/lunahealing_coverage' % os.environ.get('HOME'),
]
