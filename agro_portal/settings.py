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

HOST = 'https://agromega.in.ua'

ALLOWED_HOSTS = ['.agromega.in.ua']

WSGI_APPLICATION = 'agro_portal.wsgi.application'

# https settings
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
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

    # Package for project api: http://www.django-rest-framework.org/
    'rest_framework',

    # project apps
    'core.classifier',
    'core.pro_auth',
    'core.posts',
    'core.services',

    # Third part packages
    # Translation plugin http://django-rosetta.readthedocs.org/en/latest/index.html
    'rosetta',
    # Package for category tree realization https://github.com/django-mptt/django-mptt
    'mptt',
    # For nice working with text https://github.com/django-ckeditor/django-ckeditor
    'ckeditor',
    # For integration django and webpack https://github.com/owais/django-webpack-loader
    'webpack_loader',
    # For google ReCaptcha using: https://github.com/praekelt/django-recaptcha
    'captcha',
    # For social authentication: https://github.com/python-social-auth/social-app-django
    'social_django',

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
    'core.utils.middleware.SecurityMiddleware',
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
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect'
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

# ========================================================================================
# Authentication settings
# ========================================================================================

# Project authentication model
AUTH_USER_MODEL = 'pro_auth.User'

# Project authentication backend
AUTHENTICATION_BACKENDS = [
    'social_core.backends.open_id.OpenIdAuth',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.vk.VKOAuth2',
    'core.pro_auth.backends.AuthBackend'
]


SOCIAL_AUTH_FIELDS_STORED_IN_SESSION = ['phone1', ]


SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'pro_auth.pipeline.add_user_extra_data',
    'pro_auth.pipeline.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

# TODO: create login_url login_redirect_url

# ========================================================================================
# ReCaptcha settings
# ========================================================================================

RECAPTCHA_PUBLIC_KEY = '6LdxSyITAAAAAJNvP7eOrHlGRddLF3OgOUiAqvxj'
RECAPTCHA_PRIVATE_KEY = '6LdxSyITAAAAAJIeEbsTxqTYRAGVtFqWexypK_se'
NOCAPTCHA = True

# ========================================================================================
# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
# ========================================================================================

LANGUAGE_CODE = 'uk-Uk'

LANGUAGES = [
    ('uk', _('Ukrainian')),
    ('en', _('English')),
]

# =========================================================================================
# Model translation settings
# =========================================================================================
MODELTRANSLATION_DEFAULT_LANGUAGE = 'uk'

MODELTRANSLATION_TRANSLATION_FILES = (
    'core.classifier.translation',
    'core.posts.translation',
    'core.services.translation',
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
    os.path.join(BASE_DIR, 'assets'),
    os.path.join(BASE_DIR, 'assets/node_modules/bootstrap/dist'),
    os.path.join(BASE_DIR, 'assets/node_modules/jquery/dist'),
]

WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': 'bundles/',
        'STATS_FILE': os.path.join(BASE_DIR, 'assets/webpack-stats.json'),
    }
}

# Media files (uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


CKEDITOR_UPLOAD_PATH = '/media/ckeditor/'

# Importing security settings
from .settings_local import *  # noqa
