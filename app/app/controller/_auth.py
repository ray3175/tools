from functools import wraps
from flask import abort, request
from ..config import AppConfig
from ..service.auth import ServiceAuth


def auth(func):
    @wraps(func)
    def varify(*args, **kwargs):
        if not (xy_token:=request.headers.get(AppConfig()["web"]["key"])):
            abort(400)
        if not ServiceAuth().verify(xy_token):
            abort(401)
        return func(*args, **kwargs)
    return varify

