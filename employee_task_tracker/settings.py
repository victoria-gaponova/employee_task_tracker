import os
from datetime import timedelta

from dotenv import load_dotenv

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Чтение файла с переменными окружения
load_dotenv(BASE_DIR / ".env")
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DOMAIN_NAME = os.getenv("DOMAIN_NAME")

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "users",
    "tasks",
    "rest_framework",
    "drf_yasg",
    "django_celery_beat",
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

ROOT_URLCONF = "employee_task_tracker.urls"

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

WSGI_APPLICATION = "employee_task_tracker.wsgi.application"

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB"),  # Название БД
        "USER": os.getenv("POSTGRES_USER"),  # Пользователь для подключения
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),  # Пароль для этого пользователя
        "HOST": os.getenv("POSTGRES_HOST"),  # Адрес, на котором развернут сервер БД
        "PORT": "5432",  # Порт, на котором работает сервер БД
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Настройка проекта для работы с новой моделью пользователя
AUTH_USER_MODEL = "users.Employee"

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAdminUser",
    ]
}

# Настройки для Celery
# URL-адрес брокера сообщений
CELERY_BROKER_URL = os.getenv("CELERY_BROKER_HOST")

# URL-адрес брокера результатов, также Redis
CELERY_RESULT_BACKEND = os.getenv("CELERY_BROKER_HOST")

# Часовой пояс для работы Celery
CELERY_TIMEZONE = "Europe/Moscow"

# Флаг отслеживания выполнения задач
CELERY_TASK_TRACK_STARTED = True

# Форматы содержимого, которые Celery может принимать
CELERY_ACCEPT_CONTENT = [
    "application/json",
]

# Формат сериализации, который Celery должен использовать для сериализации результатов выполнения задач
CELERY_RESULT_SERIALIZER = "json"

# Формат сериализации для данных задач, отправляемых в Celery для выполнения
CELERY_TASK_SIRIALIZER = "json"

CELERY_BEAT_SCHEDULE = {
    "task-daily": {
        "task": "tasks.tasks.send_message",  # Путь к задаче
        "schedule": timedelta(
            hours=24
        ),  # Расписание выполнения задачи (каждые 24 часа)
    },
}
