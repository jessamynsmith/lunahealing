# Django settings for lunahealing project.
import dateutil.parser
import os

from email.utils import formataddr


BASE_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__),
                                         os.path.pardir))

ADMINS = (
    (os.environ.get('ADMIN_NAME', 'admin'), os.environ.get('ADMIN_EMAIL', 'example@example.com')),
)

# https://docs.djangoproject.com/en/1.7/topics/i18n/
TIME_ZONE = 'America/Toronto'

LANGUAGE_CODE = 'en-us'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    BASE_DIR + '/static/',
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    BASE_DIR + '/templates/',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "settings_context_processor.context_processors.settings",
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'lunahealing.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'lunahealing.wsgi.application'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'settings_context_processor',
    'pages'
]

DEFAULT_FROM_EMAIL = formataddr(ADMINS[0])
EMAIL_HOST = os.environ.get('MAILGUN_SMTP_SERVER')
EMAIL_PORT = os.environ.get('MAILGUN_SMTP_PORT')
EMAIL_HOST_USER = os.environ.get('MAILGUN_SMTP_LOGIN')
EMAIL_HOST_PASSWORD = os.environ.get('MAILGUN_SMTP_PASSWORD')
EMAIL_USE_TLS = True

DEPLOY_DATE = dateutil.parser.parse(os.environ.get('DEPLOY_DATE', ''))
VERSION = '0.1'

TEMPLATE_VISIBLE_SETTINGS = ['DEPLOY_DATE', 'VERSION']
