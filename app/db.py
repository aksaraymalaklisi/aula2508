from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from .models import Product
import os

async def init_db():
    # Cria cliente MongoDB assíncrono
    client = AsyncIOMotorClient(os.getenv("MONGODB_URI"))
    
    # Seleciona o banco de dados
    db = client[os.getenv("DB_NAME")]
    
    # Inicializa o Beanie com os modelos
    await init_beanie(database=db, document_models=[Product])