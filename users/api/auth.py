import logging
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.utils import jwt_decode_handler
from utils import baseview
from users.models import User
from users.serializers import UserSerializers

logger = logging.getLogger("ttool.app")


class LoginView(baseview.AnyLogin):
    "login view"

    def post(self, request, args=None):
        data = request.data
        if "username" not in data or "password" not in data:
            return JsonResponse({"code": 401, "data": {}, "msg": 'username or password required'})
        username = data["username"]
        password = data["password"]
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            login(request, user)
            resp = JsonResponse(
                {"code": 200,
                 "data": {"username": user.get_username(), "token": token},
                 "msg": "login success."
                 })
            return resp
        return JsonResponse({"code": 404, "data": {}, "msg": 'Unauthorized'})


class UserInfoView(baseview.BaseView):
    "user info view"

    def get(self, request, args=None):
        print(request.user)
        # authorization = request.META.get('HTTP_AUTH_KEY')
        # if authorization is not None:
        #     token = authorization.split(' ')[1]
        token = request.GET.get("token")
        if token == "":
            return JsonResponse({"code": 404, "data": {}, "msg": 'need auth-key.'})
        user_dict = jwt_decode_handler(token=token)
        user_obj = User.objects.filter(username=user_dict["username"])
        if user_obj.exists():
            serializers = UserSerializers(user_obj, many=True)
            return JsonResponse({"code": 200,
                                 "data": {"user_info": serializers.data},
                                 "msg": "get user info success"})
        return JsonResponse({"code": 404, "data": {}, "msg": 'user not exist.'})


class LogoutView(baseview.AnyLogin):
    "logout view"

    def post(self, request, args=None):
        print(request.user)
        logout(request)
        return JsonResponse({"code": 200, "data": {}, "msg": 'logout success.'})


class RegisterView(baseview.AnyLogin):
    "register user view"

    def post(self, request, args=None):
        data = request.data
        if "username" not in data or "password" not in data:
            return JsonResponse({"code": 404, "data": {}, "msg": 'username or password required'})
        username = data["username"]
        password = data["password"]
        user = User.objects.filter(username=username)
        if user.exists():
            return JsonResponse({"code": 404, "data": {}, "msg": 'username already exist.'})
        User.objects.create_user(username=username, password=password)
        return JsonResponse({"code": 200, "data": {}, "msg": 'register success.'})


class RefreshTokenView(baseview.BaseView):
    """refresh token view"""

    def post(self, request, args=None):
        print("refresh token：", request.user)
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(request.user)
        token = jwt_encode_handler(payload)
        return JsonResponse({"code": 200, "data": {'token': token}, "msg": "refresh token success"})
