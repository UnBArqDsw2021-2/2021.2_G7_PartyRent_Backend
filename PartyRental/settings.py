"""
Django settings for PartyRental project.
"""

import datetime
import os
from pathlib import Path

import environ


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
ENVFILE_PATH = os.path.join(BASE_DIR, '.env')

# Take environment variables from .env file
environ.Env.read_env(ENVFILE_PATH)

# set casting, default value DEBUG = False
env_config = environ.Env(DEBUG=(bool, False))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env_config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# False if not in os.environ because of casting above
DEBUG = env_config('DEBUG')

ALLOWED_HOSTS = [env_config("ALLOWED_HOSTS")]

AUTH_USER_MODEL = 'users.User'
# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_yasg',
    'users',
    'product',
    'shoppingcart',
    'review',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'PartyRental.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'PartyRental.wsgi.application'

if env_config("USE_DOCKER") == "True":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": env_config("POSTGRES_DB"),
            "USER": env_config("POSTGRES_USER"),
            "PASSWORD": env_config("POSTGRES_PASSWORD"),
            "HOST": env_config("POSTGRES_HOST"),
            "PORT": env_config("POSTGRES_PORT"),
        },
    }
else:
    DATABASES = {
        "default": {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'local-db.sqlite3'),
        },
    }


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=2),
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),
    'JWT_ALLOW_REFRESH': True,
#    'JWT_RESPONSE_PAYLOAD_HANDLER': '.serializers.webtoken_serializer.jwt_response_payload_handler',
}

AUTH_USER_MODEL = 'users.User'


ADMINS = [
    ['caiogabriel','caio@gmail.com'],
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )


}