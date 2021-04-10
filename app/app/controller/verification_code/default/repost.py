from flask import request, abort
from flask_cors import cross_origin
from xy.exception import XYException
from ....lib.flask.decorator import json_content_type
from ....lib.flask.response import response
from ....service.verification_code.default.repost import ServiceDefaultRepost
from .. import verification_code_blueprint
from ..._auth import auth


@verification_code_blueprint.route("/repost", methods=["GET", "POST"])
@cross_origin()
@auth
@json_content_type()
def repost():
    rsp = {
        "code": 500,
        "msg": "服务器出现未知错误，请联系管理员！"
    }
    if request.method == "GET":
        url = request.args.get("url")
        method = request.args.get("method", "GET")
        params = request.args.get("params")
        data = request.args.get("data")
        json = request.args.get("json")
    else:
        data = request.get_json()
        url = data.get("url")
        method = data.get("method", "GET")
        params = data.get("params")
        _data = data.get("data")
        json = data.get("json")
    if not url:
        abort(400)
    try:
        rsp["data"] = ServiceDefaultRepost().do_repost(url, method, params, _data, json)
        rsp["code"] = 200
        rsp["msg"] = "请求转发成功！"
    except XYException as e:
        rsp["code"] = 201
        rsp["msg"] = e.msg
    return response(**rsp)

