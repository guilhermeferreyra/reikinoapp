from uuid import uuid4
from fastapi import FastAPI
from models import User
from typing import List

app = FastAPI()

db: List[User] = [
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
        last_name = "irmão do cassio",
        email = "teste@hotmail.com",
        password = "123456",
        is_active = True 
    )
]

@app.get("/api/v1/users")
async def fetch_users():
    return db

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}