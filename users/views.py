import logging
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.views.decorators.http import require_POST
logger = logging.getLogger("app")


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
        resp.set_cookie("id", user.id)
        return resp
    return JsonResponse({"value": 'Unauthorized'}, status=401)


def logout_view(req):
    logout(req)
    return redirect("/login")


def test(req):
    print(req)
    logger.error("这是一个error日志")
    return JsonResponse({"code": 200})
