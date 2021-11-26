import logging
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from utils import baseview
from users.models import User

logger = logging.getLogger("ttool.app")


class LoginView(baseview.AnyLogin):
    "login view"

    def post(self, request, args=None):
        data = request.data
        if "username" not in data or "password" not in data:
            return JsonResponse({"code": 401, "data": {}, "msg": 'username or password required'})
        username = data["username"]
        password = data["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            resp = JsonResponse(
                {"code": 200, 
                 "data": {"username": user.get_username(), "id": user.id}, 
                 "msg": "login success."
                })
            return resp
        return JsonResponse({"code": 401, "data": {}, "msg": 'Unauthorized'})


class LogoutView(baseview.AnyLogin):
    "logout view"

    def post(self, request, args=None):
        logout(request)
        return JsonResponse({"code": 200, "data": {}, "msg": 'logout success.'})


class RegisterView(baseview.AnyLogin):
    "register user view"

    def post(self, request, args=None):
        data = request.data
        if "username" not in data or "password" not in data:
            return JsonResponse({"code": 401, "data": {}, "msg": 'username or password required'})
        username = data["username"]
        password = data["password"]
        try:
            User.objects.create_user(username=username, password=password)
        except: # pylint: disable=bare-except
            return JsonResponse({"code": 401, "data": {}, "msg": 'username already exist.'})
        return JsonResponse({"code": 200, "data": {}, "msg": 'register success.'})
