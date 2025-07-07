# app/models.py
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    password_hash: str

    seal: Optional["Seal"] = Relationship(back_populates="owner")


class Seal(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    owner_id: int = Field(foreign_key="user.id")
    name: str
    mood: int = Field(default=100)
    cleanliness: int = Field(default=100)
    last_updated: datetime = Field(default_factory=datetime.utcnow)

    owner: Optional[User] = Relationship(back_populates="seal")
