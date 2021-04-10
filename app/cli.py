import click
from flask.cli import FlaskGroup
from app import create_app


def __init_english_db():
    from app.help.init_db import InitEnglishDB
    return InitEnglishDB()


@click.group(cls=FlaskGroup, create_app=create_app)
def cli():
    pass


@cli.command()
def db_init():
    print("正在初始化数据库！")
    english_db = __init_english_db()
    english_db.create_db()
    print("数据库初始化已完成！")


@cli.command()
def db_drop():
    print("正在删除数据库！")
    english_db = __init_english_db()
    english_db.drop_db()
    print("数据库删除已完成！")


if __name__ == '__main__':
    cli()
