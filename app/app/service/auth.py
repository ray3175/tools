from xy.exception import XYWarning, XYInfo
from ..lib.cache.redis import CacheRedis
from ..lib.iam import IAM


class ServiceAuth:
    def __init__(self):
        super().__init__()

    @CacheRedis().cache("xy_token", "xy_token")
    def verify(self, xy_token):
        rsp = IAM().auth(xy_token)
        if rsp["code"] != 200:
            raise XYWarning("IAM服务器返回报文异常，异常提示：\n\t{}".format(rsp["msg"]))
        if not rsp["data"]["person_id"]:
            raise XYInfo("该账号未绑定身份信息，请先绑定再试！")
        return rsp["data"]

