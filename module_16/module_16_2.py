# Задача "Аннотация и валидация".

from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()  # создаем экземпляр приложения через конструктор


# функция-обработчик корневого GET-запроса вместе с методом-декоратором app.get
@app.get("/")
# async def read_root() -> dict:
async def read_root() -> str:
    return "Главная страница"


# функция-обработчик импровизированного GET-запроса страницы вместе с методом-декоратором app.get
@app.get("/user/admin")
async def read_admin_page() -> str:
    return "Вы вошли как администратор"


# функция-обработчик импровизированного GET-запроса пользователя вместе с валидацией входных данных.
@app.get("/user/{user_id}")
async def read_user_pages(user_id: int = Path(ge=1, le=100, description="Enter User ID")) -> str:
    return f"Вы вошли как пользователь № {user_id}"


# функция-обработчик импровизированного GET-запроса пользователя и его возраста вместе с валидацией входных данных.
@app.get("/user{username}/{age}")
async def read_users_pages(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username")],
                           age: int = Path(ge=18, le=120, description="Enter age'")) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"

# C:\Users\Yed\PycharmProjects\pythonProject\module_16> python -m uvicorn module_16_2:app
# uvicorn main:app --reload | uvicorn module_16_2:app --reload
