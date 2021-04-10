from base64 import encodebytes
from sqlalchemy import func
from ....lib.database.session import SessionEnglish
from ....modules.english.relation_category_word import RelationCategoryWord
from ....modules.english.history import History
from .. import Service
from ..history import ServiceHistory
from ..relation_category_word import ServiceRelationCategoryWord
from ..word import ServiceWord
from ..example_sentence import ServiceExampleSentence


class ServiceWordReciteWord(Service):
    WORD_TYPE = {
        "all": {
            "desc": "全部"
        },
        "new": {
            "desc": "新词"
        },
        "right": {
            "desc": "正确词汇"
        },
        "error": {
            "desc": "错误词汇"
        },
        "error-repeat": {
            "desc": "重复错误词汇"
        },
        "error-repeat-in-30-day": {
            "desc": "30天内错误词汇"
        },
        "error-repeat-in-7-day": {
            "desc": "7天内错误词汇"
        }
    }

    def __init__(self):
        super().__init__()

    def __new_history_word_conditions(self, category_id, person_id, word_type, history_time=None):
        conditions = [RelationCategoryWord.category_id == category_id, History.person_id == person_id]
        if word_type == "right":
            conditions.append(History.is_error == False)
        elif word_type == "error":
            conditions.append(History.is_error == True)
        elif word_type == "error-repeat":
            conditions.append(History.is_error_repeat == True)
        elif word_type == "error-repeat-in-30-day":
            conditions.append(History.is_error_repeat_in_30_day == True)
        elif word_type == "error-repeat-in-7-day":
            conditions.append(History.is_error_repeat_in_7_day == True)
        if history_time:
            conditions.append(func.date_format(History.time, "%Y-%m-%d") == history_time)
        return conditions

    @SessionEnglish.transaction(auto_commit=False)
    def get_word(self, category_id, person_id, word_type, word_number, word_random_mode):
        if word_type in ["all", "new"]:
            if data:=ServiceRelationCategoryWord().get_word_with_category_id_random_number(category_id, word_number) if word_type == "all" else ServiceRelationCategoryWord().get_person_new_word_with_category_id_person_id(category_id, person_id, word_number):
                data = [i.word(del_column=["audio"]) for i in data]
        else:
            conditions = self.__new_history_word_conditions(category_id, person_id, word_type)
            if data:=ServiceHistory().get_history_with_conditions_unique_relation_category_word_id(conditions, word_number):
                data = [i.relation_category_word.word(del_column=["audio"]) for i in data]
        return data

    @SessionEnglish.transaction(auto_commit=False)
    def get_history_word(self, category_id, person_id, word_type, history_time):
        conditions = self.__new_history_word_conditions(category_id, person_id, word_type, history_time)
        if data:=ServiceHistory().get_history_with_conditions(conditions):
            data = [i.relation_category_word.word(del_column=["audio"]) for i in data]
        return data

    def get_word_audio(self, word_id):
        bytes_content = ServiceWord().get_audio_with_id(word_id)
        return encodebytes(bytes_content).decode("utf-8") if bytes_content else "0"

    @SessionEnglish.transaction(auto_commit=False)
    def get_example_sentence(self, word_id):
        example_sentence_list = ServiceExampleSentence().get_example_sentence_with_word_id(word_id)
        return [example_sentence(del_column=["audio"]) for example_sentence in example_sentence_list]

    def get_example_sentence_audio(self, example_sentence_id):
        bytes_content = ServiceExampleSentence().get_audio_with_id(example_sentence_id)
        return encodebytes(bytes_content).decode("utf-8") if bytes_content else "0"

    @SessionEnglish.transaction(auto_commit=False)
    def add_recite_history(self, person_id, record):
        history_list = list()
        service_history = ServiceHistory()
        for i in record:
            relation_category_word_id = ServiceRelationCategoryWord().get_id_with_category_id_word_id(i["category_id"], i["word_id"])
            history = dict(person_id=person_id, relation_category_word_id=relation_category_word_id, time=i["time"], is_error=i["error"])
            if i["error"]:
                check_repeat_result = service_history.check_repeat_error_with_days(person_id, relation_category_word_id, [0, 30, 7])
                history.update({
                    "is_error_repeat": check_repeat_result[0],
                    "is_error_repeat_in_30_day": check_repeat_result[30],
                    "is_error_repeat_in_7_day": check_repeat_result[7]
                })
            history_list.append(history)
        return service_history.add_params_list(history_list)

