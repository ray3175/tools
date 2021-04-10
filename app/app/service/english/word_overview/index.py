from ....lib.database.session import SessionEnglish
from .. import Service
from ..category import ServiceCategory
from ..history import ServiceHistory
from ..relation_category_word import ServiceRelationCategoryWord


class ServiceWordOverviewIndex(Service):
    def __init__(self):
        super().__init__()

    @SessionEnglish.transaction(auto_commit=False)
    def get_word_overview(self, person_id):
        word_overview_list = list()
        service_histtory = ServiceHistory()
        service_relation_category_word = ServiceRelationCategoryWord()
        for category in ServiceCategory().get():
            category_name = category["name"]
            has_recite = service_histtory.get_history_unique_count_with_person_id_category_id(person_id, category["id"])
            all_word = service_relation_category_word.get_word_count_with_category_id(category["id"])
            recit_day = service_histtory.get_history_time_unique_count_with_person_id_category_id(person_id, category["id"])
            word_overview_list.append(dict(
                id=category["id"],
                name=category_name,
                recit_number=has_recite,
                all_number=all_word,
                recit_day=recit_day
            ))
        return word_overview_list

