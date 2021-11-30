# -*- coding:utf-8 -*-
'''

Some tool sets

'''
import time
from django.utils.decorators import method_decorator
from drf_yasg2.utils import swagger_auto_schema


def now():
    '''
    datetime
    '''
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


def no_method_decorator(method):
    '''
    self method decorator.
    '''
    return method_decorator(
        name=method,
        decorator=swagger_auto_schema(
            auto_schema=None,
        ),
    )
