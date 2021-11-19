# -*- coding:utf-8 -*-
'''

Some tool sets

'''
import time
import logging
import traceback
from logging.handlers import TimedRotatingFileHandler
from django.conf import settings
from django.http import HttpResponse

BASE_DIR = settings.BASE_DIR
logger = logging.getLogger("Djentry.app")


def loggerInFile():
    def decorator(func):
        def inner(*args, **kwargs):
            logFilePath = BASE_DIR+"/logs/err.log"
            logger = logging.getLogger()
            logger.setLevel(logging.INFO)
            handler = TimedRotatingFileHandler(logFilePath,
                                               when="d",
                                               interval=1,
                                               backupCount=5)
            formatter = logging.Formatter(
                '%(asctime)s  - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            try:
                return func(*args, **kwargs)
            except:
                logger.error(traceback.format_exc())
                return HttpResponse(status=500)
        return inner
    return decorator


def now():
    '''
    datetime
    '''
    now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    return now
