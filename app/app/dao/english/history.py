from sqlalchemy import func, case, distinct
from xy.utils.time import Time
from ...modules.english.history import History
from ...modules.english.relation_category_word import RelationCategoryWord
from . import DaoEnglish


class DaoHistory(DaoEnglish):
    def __init__(self, module=History):
        super().__init__(module)

    def get_history_unique_count_with_person_id_category_id(self, person_id, category_id):
        return self.session.query(func.count(distinct(History.relation_category_word_id))).filter(
            History.person_id == person_id,
            History.relation_category_word_id.in_(self.session.query(RelationCategoryWord.id).filter_by(category_id=category_id))
        ).scalar()

    def get_history_time_unique_count_with_person_id_category_id(self, person_id, category_id):
        return self.session.query(func.count(distinct(func.date_format(History.time, "%Y-%m-%d")))).filter(
            History.person_id == person_id,
            History.relation_category_word_id.in_(self.session.query(RelationCategoryWord.id).filter_by(category_id=category_id))
        ).scalar()

    def get_history_time_list_with_person_id(self, category_id, person_id, date_format, _time=None):
        conditions = [History.person_id == person_id, History.relation_category_word_id.in_(self.session.query(RelationCategoryWord.id).filter_by(category_id=category_id))]
        if _time:
            conditions.append(func.date_format(History.time, date_format[: -3]) == _time)
        return self.session.query(
            func.date_format(History.time, date_format).label("date")
        ).filter(*conditions).group_by(
            func.date_format(History.time, date_format)
        ).all()

    def get_history_statistics_with_person_id_time(self, category_id, person_id, _time):
        return self.session.query(
            func.count(History.id).label("all"),
            func.sum(case([(History.is_error == True, 1), ], else_=0)).label("error"),
            func.sum(case([(History.is_error_repeat == True, 1), ], else_=0)).label("error_repeat"),
            func.sum(case([(History.is_error_repeat_in_30_day == True, 1), ], else_=0)).label("error_repeat_in_30_day"),
            func.sum(case([(History.is_error_repeat_in_7_day == True, 1), ], else_=0)).label("error_repeat_in_7_day")
        ).filter(
            History.person_id == person_id,
            History.relation_category_word_id.in_(self.session.query(RelationCategoryWord.id).filter_by(category_id=category_id)),
            History.time.like(f"{_time}%")
        ).first()

    def get_history_statistics_list_with_person_id(self, person_id, date_format):
        return self.session.query(
            func.date_format(History.time, date_format).label("date"),
            func.count(History.id).label("all"),
            func.sum(case([(History.is_error == True, 1), ], else_=0)).label("error"),
            func.sum(case([(History.is_error_repeat == True, 1), ], else_=0)).label("error_repeat"),
            func.sum(case([(History.is_error_repeat_in_30_day == True, 1), ], else_=0)).label("error_repeat_in_30_day"),
            func.sum(case([(History.is_error_repeat_in_7_day == True, 1), ], else_=0)).label("error_repeat_in_7_day"),
        ).filter(History.person_id == person_id).group_by(func.date_format(History.time, date_format)).all()

    def get_history_with_conditions_unique_relation_category_word_id(self, conditions, limit_number):
        return self.session.query(History).filter(*conditions).group_by(History.relation_category_word_id).order_by(func.rand()).limit(limit_number).all()

    def get_history_with_conditions(self, conditions):
        return self.session.query(History).filter(*conditions).order_by(func.rand()).all()

    def check_repeat_error_by_day(self, person_id, relation_category_word_id, day):
        conditions = [History.person_id == person_id, History.relation_category_word_id == relation_category_word_id]
        if day:
            conditions.append(History.time >= (Time() - {"days": day}).to_string())
        return self.session.query(History.is_error).filter(*conditions).all()

    def add_params_list(self, params_list):
        history_obj_list = [History(**params) for params in params_list]
        self.session.add_all(history_obj_list)
        return True

