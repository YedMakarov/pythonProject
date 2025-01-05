from module_17.module_17_1.app.backend.db import Base
from sqlalchemy import Column, ForeinKey, Integer, String
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(String)
    slug = Column(String, unique=True, index=True)
    tasks =
# id - целое число, первичный ключ, с индексом.
# username - строка.
# firstname - строка.
# lastname - строка.
# age - целое число.
# slug - строка, уникальная, с индексом.
# tasks - объект связи с таблицей с таблицей Task, где back_populates='user'.
