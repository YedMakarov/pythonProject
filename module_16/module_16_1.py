# Задача "Начало пути".

from fastapi import FastAPI

# from fastapi.responses import HTMLResponse
# from fastapi.responses import JSONResponse

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


# функция-обработчик импровизированного GET-запроса пользователя вместе с методом-декоратором app.get
@app.get("/user/{user_id}")
async def read_user_pages(user_id: int) -> str:
    return f"Вы вошли как пользователь № {user_id}"


# функция-обработчик импровизированного GET-запроса пользователя и его возраста вместе с методом-декоратором app.get
@app.get("/user")
async def read_users_pages(username: str, age: int) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"

# C:\Users\Yed\PycharmProjects\pythonProject\module_16> python -m uvicorn module_16_1:app
# uvicorn main:app --reload | uvicorn module_16_1:app --reload
