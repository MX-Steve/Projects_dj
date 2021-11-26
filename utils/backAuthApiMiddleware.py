from django.utils.deprecation import MiddlewareMixin
from rest_framework_jwt.utils import jwt_decode_handler
from django.http import HttpResponse, JsonResponse
from users.models import User


class AuthApiMiddleware(MiddlewareMixin):
    """auth api middleware"""
    def process_request(self, request): # pylint: disable=no-self-use
        try:
            path = request.path
            if '/admin' not in path \
                    and '/v1/login' not in path \
                    and '/isAlive' not in path \
                    and request.method != 'GET':
                token = request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
                try:
                    user_dict = jwt_decode_handler(token=token)
                except: # pylint: disable=bare-except
                    return JsonResponse({
                        "code": 10030,
                        "msg": "用户token已过期，需要重新登录",
                        "data": []
                    })
                username = user_dict["username"]
                userObj = User.objects.filter(username=username)
                if not userObj.exists():
                    return JsonResponse({
                        "code": 10031,
                        "msg": "用户不存在，请注册",
                        "data": []
                    })
                isAcess = 1
                if isAcess == 0:
                    return HttpResponse(status=403)
            isAcess = 1
        except: # pylint: disable=bare-except
            return HttpResponse(status=500)
