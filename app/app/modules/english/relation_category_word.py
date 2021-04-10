from sqlalchemy import Column, ForeignKey, Integer, BigInteger
from sqlalchemy.orm import relationship
from ...lib.database.module import Module


class RelationCategoryWord(Module):
    __tablename__ = "relation_category_word"

    id = Column(BigInteger, primary_key=True, comment="类别 - 单词，ID")
    category_id = Column(Integer, ForeignKey("category.id", ondelete="CASCADE"), index=True, nullable=False, comment="类别ID")
    category = relationship("Category", backref="*relation_category_word_from_category*")
    word_id = Column(BigInteger, ForeignKey("word.id", ondelete="CASCADE"), index=True, nullable=False, comment="单词ID")
    word = relationship("Word", backref="*relation_category_word_from_word*")

