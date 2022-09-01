from uuid import uuid4
<<<<<<< Updated upstream
from fastapi import FastAPI
from models import User, Testimony
from typing import List

app = FastAPI()

database: List[User] = [
    
    User(
        id = uuid4(),
        first_name = "Naan",
        last_name = "Cara de maçã",
        email = "naan@gmail.com",
        password = "123456",
        is_active = True
    ),
    User(
        id = uuid4(),
        first_name = "Felipe",
        last_name = "Irmão do cassio",
        email = "teste@hotmail.com",
        password = "123456",
        is_active = True 
    )
]

@app.get("/api/v1/users")
async def fetch_users():
    return database

@app.post("/api/v1/users")
async def register_user(user: User):
    database.append(user)
=======
from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional
import mysql.connector

app = FastAPI()

users = {
    1: {
        "firt_name": "Naan",
        "last_name": "Rei Delas",
        "email": "naan@gmail.com",
        "password": "12fsfe320423",
        "is_active": "true"
    },
    2: {
        "firt_name": "Felipe",
        "last_name": "Cabeça de pica",
        "email": "felipe@gmail.bom",
        "password": "senha",
        "is_active": "true"
    }
}

class User(BaseModel):
    firt_name: str
    last_name: str
    email: str
    password: str
    is_active: bool

@app.get("/get-user/{user_id}")
def get_user(user_id : int = Path(None, description = "Digite o ID do usuário que você deseja visualizar.")):
    if user_id not in users:
        return {"Mensagem" : "Usuário não existente"}
    return users[user_id]

@app.post("/create-user/{user_id}")
def create_user(user_id : int , user : User = Path(None, description = "Digite o ID do usuário que você vai criar. Abaixo no body coloque as informações do usuário.")):
    if user_id in users: 
        return {"Erro": "Usuário já existente."}
    
    users[user_id] = user
    return user[user_id]

@app.delete("/delete-user/{user_id}")
def delete_user(user_id : int):
    if user_id not in users:
        return {"Erro" : "Usuário não existente."}

    del users[user_id]
    return {"Mensagem" : "Usuário deletado"}



# def connect_to_database():
#    mydb = mysql.connector.connect(
#    host="mariadb",
#    user="reikinoapp",
#    password="reikinoapp"
#    # database="reikinoapp"
#    )
#    return mydb

# @app.post("/api/v1/user/create_user")
# async def create_user(
#    first_name: str, 
#    last_name: str, 
#    email: str, 
#    password: str, 
#    is_active: bool
#    ):
#    mydb = connect_to_database()
#    mycursor = mydb.cursor()
#    query = "INSERT INTO reikinoapp.user (first_name, last_name, email, password, is_active) VALUES (%s, %s, %s, %s, %s)"
#    values = (first_name, last_name, email, password, is_active)
#    mycursor.execute(query, values)
#    mydb.commit()
#    return {'message': 'Usuário Criado'}
>>>>>>> Stashed changes
