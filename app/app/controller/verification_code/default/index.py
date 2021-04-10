from flask import redirect
from ....config import AppConfig
from ....lib.flask.redirect import redirect_to_endpoint
from .. import verification_code_blueprint


@verification_code_blueprint.route("/", methods=["GET"])
def _index():
    return redirect_to_endpoint("default.index")


@verification_code_blueprint.route("/index", methods=["GET"])
def index():
    return redirect(AppConfig()["web"]["url"]["login"])
