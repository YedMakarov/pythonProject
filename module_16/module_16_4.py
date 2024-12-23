# Задача "Модель пользователя".

from fastapi import FastAPI, Path, status, Body, HTTPException

from pydantic import BaseModel
from typing import List

app = FastAPI()  # создаем экземпляр приложения через конструктор

# Создаём импровизированную базу данных на основе пустого списка
users = []


class User(BaseModel):
    id: int
    username: str
    age: int


# Функция-обработчик GET-запроса выдающая зарегистрированных пользователей
@app.get("/users", response_model=List[User])
async def get_users() -> List[User]:
    return users


# # Функция-обработчик POST-запроса регистрирующая нового пользователя
@app.post("/user/{username}/{age}", response_model=User)
def add_user(username: str, age: int):
    user_id = (users[-1].id + 1) if users else 1
    print(user_id)
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user


# Функция-обработчик PUT-запроса обновляющая данные зарегистрированного пользователя
@app.put("/user/{user_id}/{username}/{age}", response_model=User)
def update_user(user_id: int, username: str, age: int):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail=f"User with ID {user_id} was not found")


# Функция-обработчик DELETE-запроса удаляющая зарегистрированного пользователя по его id
@app.delete("/user/{user_id}", response_model=User)
def delete_user(user_id: int):
    for index, user in enumerate(users):
        if user.id == user_id:
            return users.pop(index)
    raise HTTPException(status_code=404, detail=f"User with ID {user_id} was not found")


# Main
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)

# C:\Users\...\PycharmProjects\pythonProject\module_16> python -m uvicorn module_16_4:app
# uvicorn main:app --reload
