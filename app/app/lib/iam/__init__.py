import requests
from xy.exception import XYException
from ...config import AppConfig


class IAM:
    config = AppConfig()["iam"]

    key = config["key"]

    project_name = config["project_name"]
    project_auth_code = config["project_auth_code"]

    url = config["url"]
    uri_auth = config["uri"]["auth"]

    headers = {
        "project_name": project_name,
        "project_auth_code": project_auth_code
    }

    def __init__(self):
        pass

    def auth(self, xy_token):
        try:
            rsp = requests.post(self.url + self.uri_auth, json={self.key: xy_token}, headers=self.headers)
            _return = rsp.json()
        except Exception as e:
            raise XYException(str(e))
        return _return


