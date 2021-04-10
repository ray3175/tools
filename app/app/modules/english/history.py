from sqlalchemy import Column, ForeignKey, BigInteger, DateTime, Boolean
from sqlalchemy.orm import relationship
from ...lib.database.module import Module


class History(Module):
    __tablename__ = "history"

    id = Column(BigInteger, primary_key=True, comment="历史记录ID")
    person_id = Column(BigInteger, nullable=False, comment="IAM用户身份id")
    relation_category_word_id = Column(BigInteger, ForeignKey("relation_category_word.id", ondelete="CASCADE"), index=True, nullable=False, comment="类别 - 单词，ID")
    relation_category_word = relationship("RelationCategoryWord", backref="*history_from_relation_category_word*")
    time = Column(DateTime, index=True, comment="时间")
    is_error = Column(Boolean, default=False, comment="是否错误")
    is_error_repeat = Column(Boolean, default=False, comment="是否重复错误")
    is_error_repeat_in_30_day = Column(Boolean, default=False, comment="是否30天内重复错误")
    is_error_repeat_in_7_day = Column(Boolean, default=False, comment="是否7天内重复错误")

