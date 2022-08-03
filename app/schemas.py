from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: str
    is_active: bool

    class Config:
        orm_mode = True


class AttendanceBase(BaseModel):
    first_name: str
    last_name: str
    datetime: str
    testimony: str


class AttendanceCreate(AttendanceBase):
    pass


class Attendance(AttendanceBase):
    id: str
    user: User
    user_id: str

    class Config:
        orm_mode = True