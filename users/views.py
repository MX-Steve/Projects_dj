import logging
from django.http import JsonResponse
from .models import User

logger = logging.getLogger("ttool.app")


def test(req):
    logger.info(req)
    # u1 = User(username="lisi", password="123456")
    # u1.save()
    user = User.objects.create_user(username="lisi3", password="123456")
    return JsonResponse({"code": 200})
