from .. import Service
from ...auth import ServiceAuth


class ServiceDefaultAuth(Service):
    def __init__(self):
        super().__init__()

    def verify(self, xy_token):
        return ServiceAuth().verify(xy_token)

