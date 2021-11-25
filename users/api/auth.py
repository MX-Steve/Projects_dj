import logging
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from utils import baseview

logger = logging.getLogger("ttool.app")


class LoginView(baseview.AnyLogin):
    "login view"
    def post(self, request, args=None):
        email = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            resp = JsonResponse({})
            return resp
        return JsonResponse({"code": 401, "data": {}, "msg": 'Unauthorized'})

class LogoutView(baseview.AnyLogin):
    "logout view"
    def post(self,req):
        logout(req)
        return redirect("/login")
