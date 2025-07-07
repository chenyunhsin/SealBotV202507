# app/main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app import models, schemas, crud, db

app = FastAPI()

@app.on_event("startup")
async def startup():
    await db.init_db()

@app.post("/register")
async def register(user: schemas.UserCreate, session: AsyncSession = Depends(db.get_session)):
    db_user = await crud.get_user_by_username(session, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return await crud.create_user(session, user)

@app.post("/seal/adopt")
async def adopt_seal(seal: schemas.SealCreate, session: AsyncSession = Depends(db.get_session)):
    return await crud.adopt_seal(session, seal)

@app.get("/seal/status/{user_id}")
async def get_seal(user_id: int, session: AsyncSession = Depends(db.get_session)):
    return await crud.get_seal_by_user_id(session, user_id)
