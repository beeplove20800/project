from .base import *

SECRET_KEY = 'django-insecure-oxkve+727kqsw57lu$y5tcn&r%n2tc6l5frwm1=34rif(zjzbt'

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
