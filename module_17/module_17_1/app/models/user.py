from module_17.module_17_1.app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)
    tasks = relationship("Task", back_populates='user')


# id - целое число, первичный ключ, с индексом.
# username - строка.
# firstname - строка.
# lastname - строка.
# age - целое число.
# slug - строка, уникальная, с индексом.
# tasks - объект связи с таблицей с таблицей Task, где back_populates='user'.

from sqlalchemy.schema import CreateTable

print(CreateTable(User.__table__))
