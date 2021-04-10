from .. import Service
from ..history import ServiceHistory


class ServiceWordDetailReciteHistory(Service):
    def __init__(self):
        super().__init__()

    def get_my_history(self, category_id, person_id, stack, _time=None):
        service_history = ServiceHistory()
        if stack in ["0", "1", "2"]:
            date_format = "%Y" if stack == "0" else "%Y-%m" if stack == "1" else "%Y-%m-%d"
            return service_history.get_history_time_list_with_person_id(category_id, person_id, date_format, _time)
        else:
            if data:=service_history.get_history_statistics_with_person_id_time(category_id, person_id, _time):
                data["error"] = float(data["error"])
                data["error_repeat"] = float(data["error_repeat"])
                data["error_repeat_in_30_day"] = float(data["error_repeat_in_30_day"])
                data["error_repeat_in_7_day"] = float(data["error_repeat_in_7_day"])
            return data

