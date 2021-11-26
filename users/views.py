import logging
from django.http import JsonResponse
from .models import User

logger = logging.getLogger("ttool.app")


def test(req):
    logger.info(req)
    return JsonResponse({"code": 200})
