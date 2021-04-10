from flask import redirect
from ....config import AppConfig
from ....lib.flask.redirect import redirect_to_endpoint
from .. import english_blueprint


@english_blueprint.route("/", methods=["GET"])
def _index():
    return redirect_to_endpoint("default.index")


@english_blueprint.route("/index", methods=["GET"])
def index():
    return redirect(AppConfig()["web"]["url"]["login"])
