# app/crud.py
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app import models, schemas
from passlib.context import CryptContext
import bcrypt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
async def authenticate_user(session: AsyncSession, username: str, password: str):
    user = await get_user_by_username(session, username)
    if not user:
        return None
    if not bcrypt.checkpw(password.encode(), user.password_hash.encode()):
        return None
    return user
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

async def get_user_by_username(session: AsyncSession, username: str):
    result = await session.execute(select(models.User).where(models.User.username == username))
    return result.scalar_one_or_none()

async def create_user(session: AsyncSession, user: schemas.UserCreate):
    hashed_pw = hash_password(user.password)
    db_user = models.User(username=user.username, password_hash=hashed_pw)
    session.add(db_user)
    await session.commit()
    await session.refresh(db_user)
    return db_user

async def adopt_seal(session: AsyncSession, seal: schemas.SealCreate):
    db_seal = models.Seal(**seal.dict())
    session.add(db_seal)
    await session.commit()
    await session.refresh(db_seal)
    print(f"[DEBUG] Adopt Seal: {db_seal}")
    return db_seal

async def get_seal_by_user_id(session: AsyncSession, user_id: int):
    result = await session.execute(select(models.Seal).where(models.Seal.owner_id == user_id))
    print(f"[DEBUG] Get Seal: {result}")
    return result.scalar_one_or_none()
