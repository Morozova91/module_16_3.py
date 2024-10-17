# Задача "Имитация работы с БД"
from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()
users = {'1': 'Имя: Example, возраст: 18'}
# Создайте новое приложение FastAPI и сделайте CRUD запросы.
# Создайте словарь users = {'1': 'Имя: Example, возраст: 18'}
# Реализуйте 4 CRUD запроса:
# 1. get запрос по маршруту '/users', который возвращает словарь users.
@app.get("/")
async def welcome() -> dict:
    return users
@app.get("/users")
async def get_users():
    return users
# 2.post запрос по маршруту '/user/{username}/{age}', который добавляет в словарь по максимальному
# по значению ключом значение строки "Имя: {username}, возраст: {age}".
# И возвращает строку "User <user_id> is registered".
@app.post("/user/{username}/{age}")
def create_user(username: Annotated[str, Path(min_length=8,max_length=20,description="Enter your username", examples="UrbanUser")],
                          age: Annotated[int, Path(ge=18, le=100, description="Enter your age", examples="24")]) -> str:
    current_index = str(int(max(users, key=int)) + 1)
    users[current_index] = f'Имя: {username}, возраст: {age}'
    return f'User {current_index} is registered'

# 3. put запрос по маршруту '/user/{user_id}/{username}/{age}',
# который обновляет значение из словаря users под ключом user_id на строку "Имя: {username}, возраст: {age}".
# И возвращает строку "The user <user_id> is registered"
@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: Annotated[str, Path(min_length=5, max_length=20
    , description="Enter username"
    , examples= "UrbanUser")], age: Annotated[int, Path(ge=18, le=120
    , description="Enter age", examples= "24")]) -> str:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} has been updated'


# 4. delete запрос по маршруту '/user/{user_id}', который удаляет из словаря users по ключу user_id пару.
@app.delete("/user/{user_id}")
def delete_user(user_id: int)->str:
    del users[user_id]
    return f'Users with {user_id} deleted'
