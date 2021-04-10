from flask import Blueprint


verification_code_blueprint = Blueprint("default", __name__, url_prefix="/verification_code")


from .default import *

