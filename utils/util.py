# -*- coding:utf-8 -*-
'''

Some tool sets

'''
from cmath import inf
import json
import time
from django.utils.decorators import method_decorator
from drf_yasg2 import openapi
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


str_to_types = {
    "string": openapi.Schema(type=openapi.TYPE_STRING),
    "int": openapi.Schema(type=openapi.TYPE_INTEGER),
    "boolean": openapi.Schema(type=openapi.TYPE_BOOLEAN),
    "object": openapi.Schema(type=openapi.TYPE_OBJECT),
    # "array": openapi.Schema(type=openapi.TYPE_ARRAY),
    "number": openapi.Schema(type=openapi.TYPE_NUMBER),
}


def swagger_auto_schema2(req, res, info):
    '''
    rewrite swagger_auto_schema
    req:
        {
            params: {
               "pa1": "string",
               "pa2": "int",
               "pa3": "boolean" 
            },
            required:["pa1","pa2"],
        }
    res:
        {
            200: '{"code":200,"data":{},"msg":"success"}',
            ...
        }
    info: "接口描述信息"
    '''
    for p in req["params"]:
        req["params"][p] = str_to_types[req["params"][p]]
    return swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=req["required"],
            properties=req["params"]
        ),
        responses=res,
        operation_summary=info)
