"""
Django settings for newspaper project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "+%b=3=4vcv^9i!lk9r)*e&(cgkw1!1ci#v)42a$u4&2a@#hq!#"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # Django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third apps
    "bootstrap4",
    "django_extensions",
    "imagekit",
    "haystack",
    "django_summernote",
    "django_gravatar",
    # Project apps
    "apps.pages.apps.PagesConfig",
    "apps.articles.apps.ArticlesConfig",
    "apps.users.apps.UsersConfig",
    "apps.comments.apps.CommentsConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

if DEBUG:
    INSTALLED_APPS += ["debug_toolbar"]

    MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware"] + MIDDLEWARE

ROOT_URLCONF = "newspaper.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            # Common project templates
            os.path.join(BASE_DIR, "newspaper", "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                # Django context processors
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # Project context processors
                "apps.articles.context_processors.categories",
            ],
        },
    },
]

WSGI_APPLICATION = "newspaper.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "newspaper",
        "USER": "postgres",
        "PASSWORD": "password",
        "HOST": "127.0.0.1",
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LOGIN_URL = "users:login"

LOGIN_REDIRECT_URL = "pages:index"

LOGOUT_REDIRECT_URL = "pages:index"


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "newspaper", "static"),
]

MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "public", "media")


# Search settings

HAYSTACK_CONNECTIONS = {
    "default": {
        "ENGINE": "haystack.backends.whoosh_backend.WhooshEngine",
        "PATH": os.path.join(BASE_DIR, "storage", "whoosh_index"),
    },
}

HAYSTACK_SIGNAL_PROCESSOR = "haystack.signals.RealtimeSignalProcessor"


# Other settings

GRAVATAR_DEFAULT_IMAGE = "identicon"

INTERNAL_IPS = ["127.0.0.1"]

X_FRAME_OPTIONS = "SAMEORIGIN"
