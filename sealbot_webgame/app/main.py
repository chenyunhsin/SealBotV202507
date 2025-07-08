# app/main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app import models, schemas, crud, db
from fastapi.responses import FileResponse,HTMLResponse
from fastapi.staticfiles import StaticFiles
from app.seal import get_random_seal
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def serve_index():
    return FileResponse("static/index.html")

@app.get("/hello")
async def hello():
    return HTMLResponse("<h1>Hello world!</h1>")
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
    logger.debug(f"***ＯＯＯ")
    seal = await crud.get_seal_by_user_id(session, user_id)
    if not seal:
        raise HTTPException(status_code=404, detail="No seal found")
    
    image = get_random_seal()
    logger.debug(f"***{image}")
    return {
        "seal": seal,
        "image": image
    }
    
@app.post("/login")
async def login(user: schemas.UserLogin, session: AsyncSession = Depends(db.get_session)):
    db_user = await crud.authenticate_user(session, user.username, user.password)
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"user_id": db_user.id, "username": db_user.username}