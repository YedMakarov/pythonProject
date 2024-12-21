# Задача "Имитация работы с БД".

from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()  # создаем экземпляр приложения через конструктор

# Создаём импровизированную базу данных на основе словаря со значением по умоланию
users = {"1": "Имя: Example, возраст: 18"}


# Функция-обработчик корневого GET-запроса
@app.get("/")
async def read_root() -> str:
    return "Главная страница"


# Функция-обработчик GET-запроса выдающая зарегистрированных пользователей
@app.get("/users")
async def read_users() -> dict:
    return users


# Функция-обработчик GET-запроса регистрирующая нового пользователя
@app.post("/user/{username}/{age}")
async def add_user(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username")],
                   age: int = Path(ge=18, le=120, description="Enter age'")) -> str:
    current_index = str(int(max(users, key=int)) + 1)
    users[current_index] = f"Имя: {username}, возраст: {age}"
    return f"User {current_index} is registred."


# Функция-обработчик GET-запроса обновляющая данные зарегистрированного пользователя
@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID")],
                      username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username")],
                      age: int = Path(ge=18, le=120, description="Enter age'")) -> str:
    users[str(user_id)] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} has been updated."


# Функция-обработчик GET-запроса удаляющая зарегистрированного пользователя по его id
@app.delete("/user/{user_id}")
async def remove_user(user_id: int = Path(ge=1, le=100, description="Enter User ID")) -> str:
    users.pop(str(user_id))
    return f"User {user_id} has been deleted."

# C:\Users\Yed\PycharmProjects\pythonProject\module_16> python -m uvicorn module_16_3:app
# uvicorn main:app --reload | uvicorn module_16_3:app --reload
