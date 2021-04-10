from ...lib.database import DBEnglish
from .. import Dao


class DaoEnglish(Dao):
    def __init__(self, module):
        super().__init__(module)

    def init_session(self):
        self.session = DBEnglish.Session()

    def new_session(self):
        return DBEnglish.Session()

