import logging
from django.http import JsonResponse

logger = logging.getLogger("ttool.app")


def test(req):
    logger.info(req)
    return JsonResponse({"code": 200})
