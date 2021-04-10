from sqlalchemy import Column, String, Integer, SmallInteger
from ...lib.database.module import Module


class Category(Module):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, comment="类别ID")
    name = Column(String(32), unique=True, comment="名称，如考研英语")
    level = Column(SmallInteger, comment="难度等级")

