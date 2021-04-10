from ...lib.database.session import SessionEnglish
from ...dao.english.example_sentence import DaoExampleSentence
from . import Service


class ServiceExampleSentence(Service):
    def __init__(self, dao=DaoExampleSentence):
        super().__init__(dao)

    @SessionEnglish.transaction(auto_commit=False)
    def get_example_sentence_with_word_id(self, word_id):
        return self.dao.get_example_sentence_with_word_id(word_id)

    @SessionEnglish.transaction(auto_commit=False)
    def get_audio_with_id(self, example_sentence_id):
        return self.dao.get_audio_with_id(example_sentence_id)
