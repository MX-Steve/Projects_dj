import logging
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.views.decorators.http import require_POST

logger = logging.getLogger("ttool.app")


@csrf_exempt
@ensure_csrf_cookie
@require_POST
def login_view(req):
    email = req.POST.get('email', '')
    password = req.POST.get('password', '')
    user = authenticate(req, username=email, password=password)
    if user is not None:
        login(req, user)
        resp = JsonResponse({})
        return resp
    return JsonResponse({"code": 401, "data": {}, "msg": 'Unauthorized'})


def logout_view(req):
    logout(req)
    return redirect("/login")
