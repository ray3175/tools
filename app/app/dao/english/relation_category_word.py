from sqlalchemy import func, distinct
from ...modules.english.relation_category_word import RelationCategoryWord
from ...modules.english.history import History
from . import DaoEnglish


class DaoRelationCategoryWord(DaoEnglish):
    def __init__(self, module=RelationCategoryWord):
        super().__init__(module)

    def get_word_count_with_category_id(self, category_id):
        return self.session.query(func.count(RelationCategoryWord.id)).filter_by(category_id=category_id).scalar()

    def get_word_with_category_id_random_number(self, category_id, limit_number):
        return self.session.query(RelationCategoryWord).filter_by(category_id=category_id).order_by(func.rand()).limit(limit_number).all()

    def get_person_new_word_with_category_id_person_id(self, category_id, person_id, limit_number):
        return self.session.query(RelationCategoryWord).filter(RelationCategoryWord.word_id.notin_(
            self.session.query(distinct(RelationCategoryWord.word_id)).filter(RelationCategoryWord.id.in_(
                self.session.query(History.relation_category_word_id).filter(History.person_id == person_id)
            ), RelationCategoryWord.category_id == category_id)
        ), RelationCategoryWord.category_id == 1).group_by(RelationCategoryWord.word_id).order_by(func.rand()).limit(limit_number).all()

    def get_id_with_category_id_word_id(self, category_id, word_id):
        return self.session.query(RelationCategoryWord.id).filter_by(category_id=category_id, word_id=word_id).first()
