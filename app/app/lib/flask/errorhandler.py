from flask import redirect
from flask_cors import cross_origin
from xy.exception import XYException
from ... import app
from ...config import AppConfig
from .response import response


class Errorhandler:
    @staticmethod
    @app.errorhandler(400)
    @cross_origin()
    def error_400(error):
        return response(400, msg="参数有误！")

    @staticmethod
    @app.errorhandler(401)
    @cross_origin()
    def error_401(error):
        return response(401, msg="无效的权限！")

    @staticmethod
    @app.errorhandler(404)
    @cross_origin()
    def error_404(error):
        return redirect(AppConfig()["web"]["url"]["login"])

    @staticmethod
    @app.errorhandler(XYException)
    @cross_origin()
    def error_xy(error):
        return response(code=500, msg=error.msg)

