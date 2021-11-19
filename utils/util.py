# -*- coding:utf-8 -*-
'''

Some tool sets

'''
import time


def now():
    '''
    datetime
    '''
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
