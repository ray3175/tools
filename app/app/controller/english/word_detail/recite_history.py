from flask import request, abort
from flask_cors import cross_origin
from xy.exception import XYWarning
from ....config import AppConfig
from ....lib.flask.response import response
from ....service.english.word_detail.recite_history import ServiceWordDetailReciteHistory
from ....service.auth import ServiceAuth
from .. import english_word_detail_blueprint
from ..._auth import auth


@english_word_detail_blueprint.route("/recite-history", methods=["GET"])
@cross_origin()
@auth
def recite_history():
    rsp = {
        "code": 500,
        "msg": "服务器出现未知错误，请联系管理员！"
    }
    token = request.headers.get(AppConfig()["web"]["key"])
    user = ServiceAuth().verify(token)
    if not (isinstance(user, dict) and (person_id:=user.get("person_id"))):
        raise XYWarning("该账号未绑定用户身份！")
    category_id = request.args.get("category_id")
    if not category_id:
        abort(400)
    stack = request.args.get("stack", "0")
    _time = request.args.get("time")
    if isinstance(data:=ServiceWordDetailReciteHistory().get_my_history(category_id, person_id, stack, _time), (list, dict)):
        rsp["code"] = 200
        rsp["data"] = data
        rsp["msg"] = "获取单词详情成功！"
    return response(**rsp)


