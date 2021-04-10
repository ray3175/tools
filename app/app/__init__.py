import os
import datetime
import flask
from .common.global_data import GlobalData


app = flask.Flask(__name__)


def init_app():
    from .config import AppConfig
    app_config = AppConfig()
    flask_config = app_config["flask-config"]

    global_data = GlobalData()
    global_data["root_path"] = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    global_data["log_path"] = os.path.join(global_data["root_path"], "log")

    app.config["SECRET_KEY"] = flask_config["SECRET_KEY"]
    app.config["PERMANENT_SESSION_LIFETIME"] = datetime.timedelta(**flask_config["PERMANENT_SESSION_LIFETIME"])


def create_app():
    from .lib.flask.errorhandler import Errorhandler
    from .controller import verification_code_blueprint
    from .controller import english_blueprint, english_word_overview_blueprint, english_word_detail_blueprint, english_word_recite_blueprint

    app.register_blueprint(verification_code_blueprint)

    app.register_blueprint(english_blueprint)
    app.register_blueprint(english_word_overview_blueprint)
    app.register_blueprint(english_word_detail_blueprint)
    app.register_blueprint(english_word_recite_blueprint)

    return app


init_app()

