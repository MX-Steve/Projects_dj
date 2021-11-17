from typing import Optional
import grpc
from xxx.settings.common import XXX_STATISTIC_BACKEND_ADDR
from backend.proto.xxx_pb2_grpc import XxxStatisticsStub

stub_instance: Optional[XxxStatisticsStub] = None


def GetStub() -> XxxStatisticsStub:
    """Return a stub for the xxx statistic server"""
    # pylint: disable=global-statement
    global stub_instance
    # pylint: enable=global-statement
    if not stub_instance:
        chan = grpc.insecure_channel(XXX_STATISTIC_BACKEND_ADDR)
        stub_instance = XxxStatisticsStub(chan)
    return stub_instance
