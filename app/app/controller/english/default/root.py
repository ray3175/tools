from flask import request
from flask_cors import cross_origin
from xy.exception import XYWarning
from ....config import AppConfig
from ....lib.flask.response import response
from ....service.english.default.root import ServiceDefaultRoot
from ....service.auth import ServiceAuth
from .. import english_blueprint
from ..._auth import auth


@english_blueprint.route("/word-recite-echart", methods=["GET"])
@cross_origin()
@auth
def word_recite_echart():
    rsp = {
        "code": 500,
        "msg": "服务器出现未知错误，请联系管理员！"
    }
    token = request.headers.get(AppConfig()["web"]["key"])
    user = ServiceAuth().verify(token)
    if not (isinstance(user, dict) and (person_id:=user.get("person_id"))):
        raise XYWarning("该账号未绑定用户身份！")
    time_type = request.args.get("time_type", "day")
    if isinstance(data:=ServiceDefaultRoot().get_word_recite_echart_data(person_id, time_type), list):
        rsp["code"] = 200
        rsp["data"] = data
        rsp["msg"] = "获取单词背诵Echart统计数据成功！"
    return response(**rsp)


