import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

SECRET_KEY = os.getenv('SECRET_KEY')
DB_ENGINE = os.getenv('DB_ENGINE')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')

DATABASES = {
    'default': {
        'ENGINE': DB_ENGINE,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASS,
    }
}

INSTALLED_APPS = ['datacenter']

DEBUG = True

ROOT_URLCONF = "project.urls"

ALLOWED_HOSTS = ['*']


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True