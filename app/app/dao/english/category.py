from ...modules.english.category import Category
from . import DaoEnglish


class DaoCategory(DaoEnglish):
    def __init__(self, module=Category):
        super().__init__(module)

    def get_category_for_all(self):
        return self.session.query(Category).all()
