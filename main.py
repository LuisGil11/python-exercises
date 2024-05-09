from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    id: int
    username: str
    email: EmailStr

app = FastAPI()

db = {}


@app.get("/users")
def read_root():
    return db


@app.get("/users/{user_id}")
def read_item(user_id: int):
    if (user_id in db):
        return db[user_id]
    return f"User with id: #{user_id} not found."

@app.post('/users')
def create_user(user: User):
    db[user.id] = user
    print(db)
    return user

@app.patch('/users/{user_id}')
def update_user(user_id: int, user: User):
    if (user_id in db):
        db[user_id].username = user.username
        db[user_id].email = user.email
        return db[user_id]
    return f"User with id: #{user_id} not found."

@app.delete("/users/{user_id}")
def delete_item(user_id: int):
    if (user_id in db):
        deleted_user = db.pop(user_id)
        return deleted_user
    return f"User with id: #{user_id} not found."