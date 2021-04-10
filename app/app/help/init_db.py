from ..lib.database.module import Module
from ..lib.database import DBEnglish


class InitEnglishDB(DBEnglish):
    def create_database(self):
        connection = DBEnglish.engine.connect()
        connection.execute("create database if not exists tools_english default charset utf8mb4;")

    def create_db(self):
        from ..modules import english
        self.create_database()
        Module.metadata.create_all(self.engine_db)

    def drop_db(self):
        from ..modules import english
        Module.metadata.drop_all(self.engine_db)

