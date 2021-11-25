import logging
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from utils import baseview

logger = logging.getLogger("ttool.app")


class LoginView(baseview.AnyLogin):
    def post(self, req, format=None):
        email = req.POST.get('username', '')
        password = req.POST.get('password', '')
        user = authenticate(req, username=email, password=password)
        if user is not None:
            login(req, user)
            resp = JsonResponse({})
            return resp
        return JsonResponse({"code": 401, "data": {}, "msg": 'Unauthorized'})

class LogoutView(baseview.AnyLogin):
    def post(self,req):
        logout(req)
        return redirect("/login")
