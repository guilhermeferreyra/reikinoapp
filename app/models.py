from datetime import time, datetime
from uuid import uuid4, UUID
# from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
# from sqlalchemy.orm import relationship
from pydantic import BaseModel
from typing import Optional

# from database import Base

# class User(BaseModel):
#     id: Optional[UUID] = uuid4
#     first_name: str
#     last_name: str
#     email: str
#     password: str
#     is_active: bool = True


class User(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    is_active: bool
    

# class Testimony(BaseModel):
#     id: Optional[UUID] = uuid4
#     first_name: str
#     last_name: str
#     datetime: str = datetime.now()
#     testimony: str
#     therapist: str

# class User(Base):
#     __tablename__ = "user"

#     id = Column(Integer, primary_key=True, index=True)
#     first_name = Column(String)
#     last_name = Column(String)
#     email = Column(String, unique=True, index=True)
#     hashed_password = Column(String)
#     is_active = Column(Boolean, default=True)

#     testimonies = relationship("Attendance", back_populates="user")

# class Attendance(Base):
#     __tablename__ = "attendance"

#     id = Column(Integer, primary_key=True, index=True)
#     first_name = Column(String)
#     last_name = Column(String)
#     datetime = Column(String, default=datetime.now())
#     user_id = Column(Integer, ForeignKey("users.id"))
#     testimony = Column(String)

#     user = relationship("User", back_populates="testimonies")