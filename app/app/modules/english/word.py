from sqlalchemy import Column, String, BigInteger, LargeBinary
from ...lib.database.module import Module


class Word(Module):
    __tablename__ = "word"

    id = Column(BigInteger, primary_key=True, comment="单词ID")
    english = Column(String(256), unique=True, nullable=False, comment="英文")
    chinese = Column(String(256), nullable=False, comment="中文")
    phonetic_symbol = Column(String(256), comment="英标")
    img = Column(LargeBinary(length=2**16), comment="图片，二进制存储")
    audio = Column(LargeBinary(length=2**16), comment="音频，二进制存储")

