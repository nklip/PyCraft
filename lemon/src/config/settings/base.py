"""
Settings shared by every environment.

Environment-specific modules (``local``, ``test``) import everything from here
and override what differs. Values come from the environment, with local
development defaults, so the same code runs anywhere without edits.

https://docs.djangoproject.com/en/6.1/topics/settings/
"""

from pathlib import Path

import environ

# src/
BASE_DIR = Path(__file__).resolve().parents[2]
# lemon/
PROJECT_DIR = BASE_DIR.parent

env = environ.Env()
env.read_env(PROJECT_DIR / ".env")


# Security
# https://docs.djangoproject.com/en/6.1/howto/deployment/checklist/

# Anything deployed must set DJANGO_SECRET_KEY; the default exists so a fresh
# checkout runs locally without setup.
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="django-insecure-u98_e!7*21ajy6q$3ka!73^vq#i__f3hl%q(c(f^&=$hmg9$*k",
)

DEBUG = env.bool("DJANGO_DEBUG", default=False)

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=[])


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Local apps
    "api.apps.ApiConfig",
    "lemon.apps.LemonConfig",
    # Django REST Framework
    "rest_framework",
    # Provides the token model behind TokenAuthentication
    "rest_framework.authtoken",
    "django_filters",
    # djoser generates the auth endpoints and must follow rest_framework
    "djoser",
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

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

ASGI_APPLICATION = "config.asgi.application"


# Database
# https://docs.djangoproject.com/en/6.1/ref/settings/#databases
#
# The discrete variables below are the contract the mysql container image
# expects, so compose.yaml and Django read the same names from the same .env.

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": env("MYSQL_DATABASE", default="lemon"),
        "USER": env("MYSQL_USER", default="mysql_fid"),
        "PASSWORD": env("MYSQL_PASSWORD", default="mysql_fid"),
        "HOST": env("MYSQL_HOST", default="127.0.0.1"),
        "PORT": env("MYSQL_PORT", default="3306"),
        "OPTIONS": {"charset": "utf8mb4"},
    }
}


# Password validation
# https://docs.djangoproject.com/en/6.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/6.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.1/howto/static-files/

STATIC_URL = "static/"

STATICFILES_DIRS = [
    BASE_DIR / "lemon" / "static",
]


# Default primary key field type
# https://docs.djangoproject.com/en/6.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Django REST Framework
# https://www.django-rest-framework.org/api-guide/settings/

REST_FRAMEWORK = {
    "DEFAULT_FILTER_BACKENDS": [
        "rest_framework.filters.OrderingFilter",
        "rest_framework.filters.SearchFilter",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 5,
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.TokenAuthentication",
        # Used by djoser
        "rest_framework.authentication.SessionAuthentication",
    ),
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.AnonRateThrottle",
        "rest_framework.throttling.UserRateThrottle",
    ],
    "DEFAULT_THROTTLE_RATES": {
        "anon": "6/minute",
        "user": "60/minute",
    },
}

DJOSER = {
    "USER_ID_FIELD": "username",
    "LOGIN_FIELD": "email",
}
