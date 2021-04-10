from flask import request
from flask_cors import cross_origin
from xy.exception import XYException, XYInfo
from ....config import AppConfig
from ....lib.flask.decorator import json_content_type
from ....lib.flask.response import response
from ....service.english.default.auth import ServiceDefaultAuth
from .. import english_blueprint


@english_blueprint.route("/auth", methods=["POST"])
@cross_origin()
@json_content_type()
def auth():
    rsp = {
        "code": 500,
        "msg": "服务器出现未知错误，请联系管理员！"
    }
    xy_token = request.headers.get(AppConfig()["web"]["key"])
    try:
        data = ServiceDefaultAuth().verify(xy_token)
        rsp["code"] = 200
        rsp["data"] = data
        rsp["msg"] = "验证通过！"
    except XYInfo as e:
        rsp["code"] = 201
        rsp["msg"] = e.msg
    except XYException as e:
        rsp["code"] = 400
        rsp["msg"] = e.msg
    except Exception as e:
        rsp["code"] = 500
        rsp["msg"] = str(e)
    return response(**rsp)


