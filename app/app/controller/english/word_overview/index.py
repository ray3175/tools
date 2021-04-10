from flask import request
from flask_cors import cross_origin
from xy.exception import XYWarning
from ....config import AppConfig
from ....lib.flask.response import response
from ....service.english.word_overview.index import ServiceWordOverviewIndex
from ....service.auth import ServiceAuth
from .. import english_word_overview_blueprint
from ..._auth import auth


@english_word_overview_blueprint.route("/", methods=["GET"])
@cross_origin()
@auth
def index():
    rsp = {
        "code": 500,
        "msg": "服务器出现未知错误，请联系管理员！"
    }
    token = request.headers.get(AppConfig()["web"]["key"])
    user = ServiceAuth().verify(token)
    if not (isinstance(user, dict) and (person_id:=user.get("person_id"))):
        raise XYWarning("该账号未绑定用户身份！")
    if isinstance(data:=ServiceWordOverviewIndex().get_word_overview(person_id), list):
        rsp["code"] = 200
        rsp["data"] = data
        rsp["msg"] = "获取单词概览成功！"
    return response(**rsp)


