from database import users
from fastapi import FastAPI, Path
from uuid import uuid4
from models import User

app = FastAPI()

@app.get("/get-database")
def get_database():
    return users

@app.get("/get-user/{user_id}")
def get_user(user_id : str):
    if user_id not in users:
        return {"Mensagem" : "Usuário não existente."}

    return users[user_id]

@app.post("/create-user")
def create_user(user : User):
    user_id = str(uuid4())

    first_name = user.first_name
    last_name = user.last_name
    email = user.email
    password = user.password
    is_active = user.is_active

    users[user_id] = {"id" : user_id, "first_name" : first_name, "last_name" : last_name, "email" : email, "password" : password, "is_active" : bool(is_active)}

    return {"Mensagem" : "Usuário criado com sucesso!"}

@app.put("/update-user")
def update_user(user_id : str, user : User):

    first_name = user.first_name
    last_name = user.last_name
    email = user.email
    password = user.password
    is_active = user.is_active

    users[user_id] = {"id" : user_id, "first_name" : first_name, "last_name" : last_name, "email" : email, "password" : password, "is_active" : bool(is_active)}

    return {"Mensagem" : "Usuário formatado com sucesso!"}


@app.delete("/delete-user/{user_id}")
def delete_user(user_id : str):
    if user_id not in users:
        return {"Erro" : "Usuário não existente."}

    del users[user_id]
    return {"Mensagem" : "Usuário deletado com sucesso!"}
