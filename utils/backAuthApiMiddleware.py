from django.utils.deprecation import MiddlewareMixin
from users.models import *
from users.serializers import *
from users.views import *
from rest_framework_jwt.utils import jwt_decode_handler
from django.http import HttpResponse, JsonResponse


class AuthApiMiddleware(MiddlewareMixin):
    def process_request(self, request):
        try:
            path = request.path
            if '/admin' not in path \
                    and '/auth/login/' not in path \
                    and '/isAlive/' not in path \
                    and request.method != 'GET':
                token = request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
                try:
                    user_dict = jwt_decode_handler(token=token)
                except:
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
        except:
            return HttpResponse(status=500)
