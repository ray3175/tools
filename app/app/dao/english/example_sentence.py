from ...modules.english.example_sentence import ExampleSentence
from . import DaoEnglish


class DaoExampleSentence(DaoEnglish):
    def __init__(self, module=ExampleSentence):
        super().__init__(module)

    def get_example_sentence_with_word_id(self, word_id):
        return self.session.query(ExampleSentence).filter_by(word_id=word_id).all()

    def get_audio_with_id(self, example_sentence_id):
        return self.session.query(ExampleSentence.audio).filter_by(id=example_sentence_id).scalar()
