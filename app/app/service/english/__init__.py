from ...lib.database.session import SessionEnglish
from ...dao.english import DaoEnglish


class Service:
    def __init__(self, dao=None):
        self.dao = dao() if callable(dao) else dao

    def new_dao(self, module=None):
        self.dao = DaoEnglish(module)

    @SessionEnglish.transaction(auto_commit=False)
    def get(self, condition=None, offset=None, limit=None, reverse=False, condition_like=False, add_column=[], del_column=[]):
        return [module(add_column=add_column, del_column=del_column) for module in self.dao.get(condition, offset, limit, reverse, condition_like)]

    @SessionEnglish.transaction
    def add(self, params):
        return self.dao.add(params)

    @SessionEnglish.transaction
    def update(self, condition, params):
        return self.dao.update(condition, params)

    @SessionEnglish.transaction
    def delete(self, condition):
        return self.dao.delete(condition)

