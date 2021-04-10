from ...modules.english.word import Word
from . import DaoEnglish


class DaoWord(DaoEnglish):
    def __init__(self, module=Word):
        super().__init__(module)

    def get_audio_with_id(self, word_id):
        return self.session.query(Word.audio).filter_by(id=word_id).scalar()
