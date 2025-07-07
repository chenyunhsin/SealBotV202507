# app/schemas.py
from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True

class SealCreate(BaseModel):
    owner_id: int
    name: str

class SealOut(BaseModel):
    id: int
    owner_id: int
    name: str
    mood: int
    cleanliness: int

    class Config:
        orm_mode = True
