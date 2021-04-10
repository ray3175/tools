from ...lib.database.session import SessionEnglish
from ...dao.english.relation_category_word import DaoRelationCategoryWord
from . import Service


class ServiceRelationCategoryWord(Service):
    def __init__(self, dao=DaoRelationCategoryWord):
        super().__init__(dao)

    @SessionEnglish.transaction(auto_commit=False)
    def get_word_count_with_category_id(self, category_id):
        return self.dao.get_word_count_with_category_id(category_id)

    @SessionEnglish.transaction(auto_commit=False)
    def get_word_with_category_id_random_number(self, category_id, limit_number):
        return self.dao.get_word_with_category_id_random_number(category_id, limit_number)

    @SessionEnglish.transaction(auto_commit=False)
    def get_person_new_word_with_category_id_person_id(self, category_id, person_id, limit_number):
        return self.dao.get_person_new_word_with_category_id_person_id(category_id, person_id, limit_number)

    @SessionEnglish.transaction(auto_commit=False)
    def get_id_with_category_id_word_id(self, category_id, word_id):
        return (relation_category_word:=self.dao.get_id_with_category_id_word_id(category_id, word_id)) and relation_category_word.id
