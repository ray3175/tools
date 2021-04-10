from ....lib.database.session import SessionEnglish
from .. import Service
from ..history import ServiceHistory


class ServiceDefaultRoot(Service):
    def __init__(self):
        super().__init__()

    @SessionEnglish.transaction(auto_commit=False)
    def get_word_recite_echart_data(self, person_id, time_type):
        date_format = "%Y" if time_type == "year" else "%Y-%m" if time_type == "month" else "%Y-%m-%d"
        _return = list()
        if data:=ServiceHistory().get_history_statistics_list_with_person_id(person_id, date_format):
            for i in data:
                _return.append({
                    "date": i.date,
                    "all": i.all,
                    "error": float(i.error),
                    "error_repeat": float(i.error_repeat),
                    "error_repeat_in_30_day": float(i.error_repeat_in_30_day),
                    "error_repeat_in_7_day": float(i.error_repeat_in_7_day),
                })
        return _return

