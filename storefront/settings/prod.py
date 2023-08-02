import os
import dj_database_url
from .common import *

DEBUG = False

REDIS_URL = env('REDIS_URL')

CELERY_BROKER_URL = REDIS_URL


CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': REDIS_URL,
        'TIMEOUT': 10 * 60,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

DATABASES = {
    'default': dj_database_url.parse(env('DATABASE_URL'))
}

SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = []