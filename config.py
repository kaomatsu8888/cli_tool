from peewee import SqliteDatabase, Model, CharField, IntegerField

# データベースの設定
db = SqliteDatabase("users_management.db")

class User(Model):
    name = CharField()
    age = IntegerField()

    class Meta:
        database = db

# テーブルを作成
db.create_tables([User])