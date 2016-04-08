"""
Django settings for golub_portal project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from django.utils.translation import ugettext_lazy as _

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v$rhqt_l$w55_wg4yz6yz&$#g@7$7_im0=r&$*dcx=8ei#)%yq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

HOST = 'http://agromega.in.ua'

ALLOWED_HOSTS = ['agromega.in.ua', ]

WSGI_APPLICATION = 'agro_portal.wsgi.application'
# Application definition

INSTALLED_APPS = [
    # Autocomplete field. https://github.com/yourlabs/django-autocomplete-light.
    'dal',
    'dal_select2',
    # Package for model fields translation
    # http://django-modeltranslation.readthedocs.org/en/latest/installation.html
    'modeltranslation',
    # Standard django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # project apps
    'appl.classifier',
    'appl.pro_auth',
    'appl.posts',

    # Third part packages
    # Translation plugin http://django-rosetta.readthedocs.org/en/latest/index.html
    'rosetta',
    # Package for category tree realization https://github.com/django-mptt/django-mptt
    'mptt',
    # For nice working with text https://github.com/django-ckeditor/django-ckeditor
    'ckeditor',
    # For integration django and webpack https://github.com/owais/django-webpack-loader
   # 'webpack_loader',

    # additional apps
    # Package for testing falling data in models https://github.com/rbarrois/factory_boy
    'factory',
]

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'agro_portal.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "agrodb",
        'USER': 'agr',
        'PASSWORD': '787898',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

# Project authentication model
AUTH_USER_MODEL = 'pro_auth.User'

# Project authentication backend
AUTHENTICATION_BACKENDS = ['appl.pro_auth.backends.AuthBackend']

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'uk-Uk'

LANGUAGES = [
    ('uk', _('Ukrainian')),
    ('en', _('English')),
]

MODELTRANSLATION_DEFAULT_LANGUAGE = 'uk'

MODELTRANSLATION_TRANSLATION_FILES = (
    'appl.classifier.translation',
    'appl.posts.translation',
)

LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale'), ]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR + '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'assets')
]

#WEBPACK_LOADER = {
#    'DEFAULT': {
#        'BUNDLE_DIR_NAME': 'bundles/',
#        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
#    }
#}

# Media files (uploads)
MEDIA_URL = '/uploads/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')


CKEDITOR_UPLOAD_PATH = '/uploads/ckeditor/'
