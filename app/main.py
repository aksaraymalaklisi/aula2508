import os
from fastapi import FastAPI
from dotenv import load_dotenv
from .db import init_db
from .routers import products

load_dotenv()
app = FastAPI(title="MongoDB + FastAPI")

@app.on_event("startup")
async def on_startup():
    await init_db()
    
app.include_router(products.router)