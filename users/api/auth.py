import json
import logging
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from drf_yasg2 import openapi
from drf_yasg2.utils import swagger_auto_schema
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.utils import jwt_decode_handler
from utils import baseview
from utils.util import no_method_decorator, swagger_auto_schema2
from users.models import User
from users.serializers import UserSerializers

logger = logging.getLogger("ttool.app")


@no_method_decorator("get")
@no_method_decorator("put")
@no_method_decorator("delete")
class LoginView(baseview.AnyLogin):
    '''
    post:
        login post view
    get:
        login get view
    '''
    # @swagger_auto_schema(
    #     request_body=openapi.Schema(
    #         type=openapi.TYPE_OBJECT,
    #         required=['username', 'password'],
    #         properties={
    #             'username': openapi.Schema(type=openapi.TYPE_STRING),
    #             'password': openapi.Schema(type=openapi.TYPE_STRING),
    #         }
    #     ),
    #     responses={200: json.dumps({"code": 200, "msg": "login success", "data": {
    #                                "username": "lisi", "token": "xxxx...."}}),
    #                401: json.dumps({"code": 404, "data": {}, "msg": 'Unauthorized'})},
    # operation_summary='用户登陆接口')
    @swagger_auto_schema2(
        req={"required": ['username', 'password'],
             "params": {"username": 'string', "password": 'string'}},
        info="登陆接口",
        res={200: json.dumps({"code": 200, "msg": "login success", "data": {
            "username": "lisi", "token": "xxxx...."}})})
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


@no_method_decorator("post")
@no_method_decorator("put")
@no_method_decorator("delete")
class UserInfoView(baseview.BaseView):
    "user info view"

    def get(self, request, args=None):
        token = ""
        authorization = request.META.get('HTTP_AUTHORIZATION')
        if authorization is not None:
            token = authorization.split(' ')[1]
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


@no_method_decorator("get")
@no_method_decorator("put")
@no_method_decorator("delete")
class LogoutView(baseview.BaseView):
    "logout view"

    def post(self, request, args=None):
        print(request.user)
        logout(request)
        return JsonResponse({"code": 200, "data": {}, "msg": 'logout success.'})


@no_method_decorator("get")
@no_method_decorator("put")
@no_method_decorator("delete")
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


@no_method_decorator("get")
@no_method_decorator("put")
@no_method_decorator("delete")
class RefreshTokenView(baseview.BaseView):
    """refresh token view"""

    def post(self, request, args=None):
        print("refresh token：", request.user)
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(request.user)
        token = jwt_encode_handler(payload)
        return JsonResponse({"code": 200, "data": {'token': token}, "msg": "refresh token success"})
