# Задача "Модель пользователя".

from fastapi import FastAPI, Path, status, Body, HTTPException
# from typing import Annotated
from pydantic import BaseModel
from typing import List

app = FastAPI()  # создаем экземпляр приложения через конструктор

# Создаём импровизированную базу данных на основе пустого списка
users = []


class User(BaseModel):
    id: int = None
    username: str = None
    age: int = None


# Функция-обработчик GET-запроса выдающая зарегистрированных пользователей
@app.get("/users")
async def read_users() -> List[User]:
    return users


# # Функция-обработчик GET-запроса регистрирующая нового пользователя
@app.post("/user/{username}/{age}")
def add_user(user_: User, username: str, age: int) -> str:
    user_.id = len(users) + 1
    user_.username = username
    user_.age = age
    users.append(user_)
    return f"User with name {user_.username} and age {user_.age} year(s) is created."


# Функция-обработчик GET-запроса обновляющая данные зарегистрированного пользователя
@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_: User, user_id: int, username: str, age: int) -> str:
    try:
        user_.id = user_id
        users[user_id].username = user_.username
        users[user_id].age = user_.age
        return f"User with ID update name to {user_.username} and age to {user_.age} year(s)."
    except IndexError:
        raise HTTPException(status_code=404, detail=f"User with ID {user_.id} is not found")


# Функция-обработчик GET-запроса удаляющая зарегистрированного пользователя по его id
@app.delete("/user/{user_id}")
async def remove_user(user_: User, user_id: int) -> str:
    try:
        user_.id = user_id
        users.pop(user_.id)
        return f"User with ID {user_.id} is deleted."
    except IndexError:
        raise HTTPException(status_code=404, detail=f"User with ID {user_.id} is not found")

# C:\Users\Yed\PycharmProjects\pythonProject\module_16> python -m uvicorn module_16_4:app
# uvicorn main:app --reload | uvicorn module_16_4:app --reload
