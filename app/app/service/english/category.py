from ...lib.database.session import SessionEnglish
from ...dao.english.category import DaoCategory
from . import Service


class ServiceCategory(Service):
    def __init__(self, dao=DaoCategory):
        super().__init__(dao)

    @SessionEnglish.transaction(auto_commit=False)
    def get_category_for_all(self):
        return [category() for category in self.dao.get_category_for_all()]
