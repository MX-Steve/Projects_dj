# pylint: disable=wildcard-import,unused-wildcard-import
from os import environ
from pathlib import Path
from djentry.settings.common import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = environ.get('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'clover',
        'HOST': "127.0.0.1",
        'PORT': 3306,
        'USER': "root",
        'PASSWORD': "kaituozhe520",
    }
}
