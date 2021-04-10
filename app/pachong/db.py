from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.pool import NullPool
from modules.word import Word
from modules.example_sentence import ExampleSentence
from modules.category import Category
from modules.relation_category_word import RelationCategoryWord


class DB:
    SCHEME = "mysql+pymysql"
    USER = "root"
    PASSWORD = "123456"
    HOST = "127.0.0.1"
    PORT = "3306"
    DB = "tools_english"
    CHARSET = "utf8mb4"
    url = "{scheme}://{user}:{password}@{host}:{port}/{db}?charset={charset}".format(scheme=SCHEME, user=USER, password=PASSWORD, host=HOST, port=PORT, db=DB, charset=CHARSET)
    engine = create_engine(url, pool_recycle=3600, poolclass=NullPool, encoding="utf-8")
    Session = scoped_session(sessionmaker(autoflush=False, bind=engine))

    def __init__(self, init_db=False):
        from modules import Module
        from modules.history import History

        if init_db:
            Module.metadata.drop_all(self.engine)
            Module.metadata.create_all(self.engine)

    def write_data_in_db(self, data):
        session = self.Session()
        for _class in data:
            name = _class["name"]
            word_list = _class["word_list"]
            if not (category:=session.query(Category).filter_by(name=name).first()):
                category = Category(
                    name=name
                )
                session.add(category)
                session.flush()
            category_id = category.id
            for word in word_list:
                if not (word_obj:=session.query(Word).filter_by(english=word["english"]).first()):
                    word_obj = Word(
                        english=word["english"],
                        chinese=word["chinese"],
                        phonetic_symbol=word["phonetic_symbol"],
                        audio=word["audio"]
                    )
                    session.add(word_obj)
                    session.flush()
                word_id = word_obj.id
                if not session.query(RelationCategoryWord).filter_by(category_id=category_id, word_id=word_id).first():
                    session.add(RelationCategoryWord(
                        category_id=category_id,
                        word_id=word_id
                    ))
                example_sentence_obj_list = session.query(ExampleSentence).filter_by(word_id=word_id).all()
                for example_sentence in word["example_sentence"]:
                    will_all = True
                    for example_sentence_obj in example_sentence_obj_list:
                        if example_sentence["english"] == example_sentence_obj.english:
                            will_all = False
                            break
                    if will_all:
                        session.add(ExampleSentence(
                            word_id=word_id,
                            english=example_sentence["english"],
                            chinese=example_sentence["chinese"],
                            audio=example_sentence["audio"]
                        ))
            session.commit()
            return True




