from module_17.module_17_1.app.backend.db import Base
from sqlalchemy import Column, ForeinKey, Integer, String, Bolean
from sqlalchemy.orm import relationship


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, defailt=0)
    completed = Column(Bolean, default=True)
    user_id = Column(Integer, )
    slug = Column(String, unique=True, index=True)
    user =

# id - целое число, первичный ключ, с индексом.
# title - строка.
# content - строка.
# priority - целое число, по умолчанию 0.
# completed - булевое значение, по умолчанию False.
# user_id - целое число, внешний ключ на id из таблицы 'users', не NULL, с индексом.
# slug - строка, уникальная, с индексом.
# user - объект связи с таблицей с таблицей User, где back_populates='tasks'.
