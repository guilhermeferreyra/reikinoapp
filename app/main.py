import datetime
from uuid import uuid4, UUID
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session


import models
import schemas
import database

models.Base.metadata.create_all(bind=engine)

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
        last_name = "irmão do cassio",
        email = "teste@hotmail.com",
        password = "123456",
        is_active = True 
    )
]

# @app.get("/api/v1/users")
# async def fetch_users():
#     return database
