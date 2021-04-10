from ...lib.database.session import SessionEnglish
from ...dao.english.history import DaoHistory
from . import Service


class ServiceHistory(Service):
    def __init__(self, dao=DaoHistory):
        super().__init__(dao)

    @SessionEnglish.transaction(auto_commit=False)
    def get_history_unique_count_with_person_id_category_id(self, person_id, category_id):
        return self.dao.get_history_unique_count_with_person_id_category_id(person_id, category_id)

    @SessionEnglish.transaction(auto_commit=False)
    def get_history_time_unique_count_with_person_id_category_id(self, person_id, category_id):
        return self.dao.get_history_time_unique_count_with_person_id_category_id(person_id, category_id)

    @SessionEnglish.transaction(auto_commit=False)
    def get_history_time_list_with_person_id(self, category_id, person_id, date_format, _time):
        return [history_time.date for history_time in self.dao.get_history_time_list_with_person_id(category_id, person_id, date_format, _time)]

    @SessionEnglish.transaction(auto_commit=False)
    def get_history_statistics_with_person_id_time(self, category_id, person_id, _time):
        history_statistics = self.dao.get_history_statistics_with_person_id_time(category_id, person_id, _time)
        return dict(
            all=history_statistics.all,
            error=history_statistics.error,
            error_repeat=history_statistics.error_repeat,
            error_repeat_in_30_day=history_statistics.error_repeat_in_30_day,
            error_repeat_in_7_day=history_statistics.error_repeat_in_7_day
        )

    @SessionEnglish.transaction(auto_commit=False)
    def get_history_statistics_list_with_person_id(self, person_id, date_format):
        return self.dao.get_history_statistics_list_with_person_id(person_id, date_format)

    @SessionEnglish.transaction(auto_commit=False)
    def get_history_with_conditions_unique_relation_category_word_id(self, conditions, limit_number):
        return self.dao.get_history_with_conditions_unique_relation_category_word_id(conditions, limit_number)

    @SessionEnglish.transaction(auto_commit=False)
    def get_history_with_conditions(self, conditions):
        return self.dao.get_history_with_conditions(conditions)

    @SessionEnglish.transaction(auto_commit=False)
    def check_repeat_error_with_days(self, person_id, relation_category_word_id, days):
        check_repeat_result = dict()
        for day in days:
            history_list = self.dao.check_repeat_error_by_day(person_id, relation_category_word_id, day)
            check_repeat_result.update({day: any([history.is_error for history in history_list])})
        return check_repeat_result

    @SessionEnglish.transaction
    def add_params_list(self, params_list):
        return self.dao.add_params_list(params_list)

