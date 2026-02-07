from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, text
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,   # kiểm tra connection trước khi dùng
    pool_recycle=300,     # recycle connection sau 5 phút
)

@app.get("/")
def home():
    return {"status": "API GAS RUNNING"}

@app.get("/users")
def get_users():
    with engine.connect() as conn:
        rs = conn.execute(text("SELECT id, name FROM users"))
        return [{"id": r.id, "name": r.name} for r in rs]
