import requests
from json import loads
from xy.exception import XYWarning
from .. import Service


class ServiceDefaultRepost(Service):
    def __init__(self):
        super().__init__()

    def do_repost(self, url, method="GET", params=None, data=None, json=None):
        try:
            if isinstance(params, str):
                params = loads(params)
            if isinstance(data, str):
                data = loads(data)
            if isinstance(json, str):
                data = loads(json)
            rsp = requests.request(method, url, params=params, data=data, json=json)
            _return = rsp.text
        except Exception as e:
            raise XYWarning(str(e))
        return _return


