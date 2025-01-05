# Задача "Список пользователей в шаблоне".

from fastapi import FastAPI, Path, status, Body, HTTPException, Request
from typing import Annotated
from pydantic import BaseModel
from typing import List
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

# app = FastAPI()  # создаем экземпляр приложения через конструктор
app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True}, debug=True)

# Настраиваем папку с шаблонами
templates = Jinja2Templates(directory="templates")

# Создаём импровизированную базу данных на основе пустого списка
users = []


class User(BaseModel):
    id: int
    username: str
    age: int


# Инициализация пользователей
# users.append(User(id=1, username="UrbanUser ", age=24))
# users.append(User(id=2, username="UrbanTest", age=22))
# users.append(User(id=3, username="Capybara", age=60))


# Функция-обработчик GET-запроса главной страницы
@app.get("/", response_class=HTMLResponse)
async def get_main_page(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


# Функция-обработчик GET-запроса выдающая зарегистрированных пользователей + Jinja2
@app.get("/user/{user_id}", response_class=HTMLResponse)
async def get_user(request: Request, user_id: int):
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse("users.html", {"request": request, "user": user})
    raise HTTPException(status_code=404, detail="User  not found")


# # Функция-обработчик POST-запроса регистрирующая нового пользователя
@app.post("/user/{username}/{age}", response_model=User)
def add_user(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username")],
             age: int = Path(ge=18, le=120, description="Enter age'")):
    user_id = (users[-1].id + 1) if users else 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user


# Функция-обработчик PUT-запроса обновляющая данные зарегистрированного пользователя
@app.put("/user/{user_id}/{username}/{age}", response_model=User)
def update_user(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID")],
                username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username")],
                age: int = Path(ge=18, le=120, description="Enter age")):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail=f"User with ID {user_id} was not found")


# Функция-обработчик DELETE-запроса удаляющая зарегистрированного пользователя по его id
@app.delete("/user/{user_id}", response_model=User)
def delete_user(user_id: int = Path(ge=1, le=100, description="Enter User ID")):
    for index, user in enumerate(users):
        if user.id == user_id:
            return users.pop(index)
    raise HTTPException(status_code=404, detail=f"User with ID {user_id} was not found")


# Main
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)

# C:\Users\...\PycharmProjects\pythonProject\module_16> python -m uvicorn module_16_5:app
# uvicorn main:app --reload
