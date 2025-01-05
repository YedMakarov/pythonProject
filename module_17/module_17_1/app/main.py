from fastapi import FastAPI
from routers import task
from routers import user

app = FastAPI()


@app.get("/")
async def welcome():
    return {"messagr": "Welcome to Taskmanager"}


app.include_router(user.router)
app.include_router(task.router)

# Main
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)

# C:\Users\...\PycharmProjects\pythonProject\module_16> python -m uvicorn main:app
# uvicorn main:app --reload
