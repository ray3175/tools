from sqlalchemy import Column, ForeignKey, BigInteger, LargeBinary, Text
from sqlalchemy.orm import relationship
from ...lib.database.module import Module


class ExampleSentence(Module):
    __tablename__ = "example_sentence"

    id = Column(BigInteger, primary_key=True, comment="单词例句ID")
    word_id = Column(BigInteger, ForeignKey("word.id", ondelete="CASCADE"), index=True, nullable=False, comment="单词ID")
    word = relationship("Word", backref="*example_sentence_from_word*")
    english = Column(Text, comment="例句英文")
    chinese = Column(Text, comment="例句中文")
    img = Column(LargeBinary(length=2**16), comment="图片，二进制存储")
    audio = Column(LargeBinary(length=(2**32)-1), comment="音频，二进制存储")

