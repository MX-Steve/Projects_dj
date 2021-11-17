# pylint: disable=wildcard-import,unused-wildcard-import
from os import environ
import pymysql
from xxx.settings.common import *

pymysql.install_as_MySQLdb()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = environ.get('DJANGO_SECRET_KEY')

ALLOWED_HOSTS = ["*.corp.alt-chain.io"]

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': environ.get("CLOVER_MYSQL_DB"),
        'USER': environ.get("CLOVER_MYSQL_USER"),
        'PASSWORD': environ.get("CLOVER_MYSQL_PASSWORD"),
        'HOST': environ.get("CLOVER_MYSQL_HOST"),
        'PORT': environ.get("CLOVER_MYSQL_PORT") or '3306'
    }
}
