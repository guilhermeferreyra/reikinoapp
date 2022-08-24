from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    id: int
    first_name: str
    last_name: str
    hashed_password: str
uvcxz\cz gi    
    # id = Column(Integer, primary_key=True, index=True)
    # first_name = Column(String(255), nullable=False)
    # last_name = Column(String(255), nullable=False)
    # email = Column(String(255), unique=True, index=True, nullable=False)
    # hashed_password = Column(String(255), nullable=False)
    # is_active = Column(Boolean, default=True)


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
    create_date: str
    testimony: str


class AttendanceCreate(AttendanceBase):
    pass


class Attendance(AttendanceBase):
    id: str
    user: User
    user_id: str

    class Config:
        orm_mode = True