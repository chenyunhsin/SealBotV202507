# app/db.py
from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")


engine = create_async_engine(DATABASE_URL, echo=True, future=True)
async_session = async_sessionmaker(engine, expire_on_commit=False)

async_session_maker = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

async def get_session() -> AsyncSession:
    async with async_session_maker() as session:
        yield session