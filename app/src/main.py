import datetime
from uuid import uuid4, UUID
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session


from models import *
from schemas import *
from database import SessionLocal, engine

app = FastAPI()

# @app.get("/api/v1/users")
# async def fetch_users():
#     return database

# @app.post("/api/v1/users")
# async def create_user():
#     return {"message": "ok"}