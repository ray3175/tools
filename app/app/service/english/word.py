from ...lib.database.session import SessionEnglish
from ...dao.english.word import DaoWord
from . import Service


class ServiceWord(Service):
    def __init__(self, dao=DaoWord):
        super().__init__(dao)

    @SessionEnglish.transaction(auto_commit=False)
    def get_audio_with_id(self, word_id):
        return self.dao.get_audio_with_id(word_id)

