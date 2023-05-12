from pathlib import Path
from typing import List

import django_stubs_ext
import environ
from django.utils.translation import gettext_lazy as _

BASE_DIR = Path(__file__).resolve().parent.parent


env = environ.Env()
env.read_env(str(BASE_DIR / ".env"))

django_stubs_ext.monkeypatch()


SECRET_KEY = env.str("DJANGO_SECRET_KEY")


DEBUG = True

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": lambda request: True,
}

ALLOWED_HOSTS: List[str] = []

INTERNAL_IPS = ["127.0.0.1"]


LOGIN_REDIRECT_URL = "cars"
LOGOUT_REDIRECT_URL = "cars"
LOGIN_URL = "login"


EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

CAPTCHA_IMAGE_SIZE = (100, 25)
CAPTCHA_LENGTH = 5
CAPTCHA_BACKGROUND_COLOR = "#b6cbce"
CAPTCHA_FOREGROUND_COLOR = "#022a30"

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.postgres",
    "django_cleanup.apps.CleanupConfig",
    "django_countries",
    "django.contrib.humanize",
    "phonenumber_field",
    "captcha",
    "debug_toolbar",
    "crispy_forms",
    "crispy_bootstrap5",
    "cars.apps.CarsConfig",
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [str(BASE_DIR / "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env.str("POSTGRES_DB"),
        "USER": env.str("POSTGRES_USER"),
        "PASSWORD": env.str("POSTGRES_PASSWORD"),
        "HOST": "postgres",
        "PORT": "5432",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_TZ = True
LANGUAGES = [("ru", _("Russian")), ("en", _("English"))]
LOCALE_PATHS = [str(BASE_DIR / "locale")]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

STATIC_URL = "static/"
STATICFILES_DIRS = [str(BASE_DIR / "static")]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
