# -*- coding:utf-8 -*-
from django.http import HttpResponse
from rest_framework.response import Response
from django.db import connection
from utils import baseview


class check(baseview.AnyLogin):
    "check the app status"

    def get(self, request, args=None):
        try:
            sql = "show tables;"
            cursor = connection.cursor()
            cursor.execute(sql)
            cursor.fetchone()
            return Response({'isAlive': True})
        except Exception as e:
            return HttpResponse({"data": {}, "code": 500, "msg": e}, status=500)
