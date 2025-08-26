from beanie import Document
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

# Modelo para entrada de dados
class ProductIn(BaseModel):
    name: str = Field(min_length=2)
    price: float = Field(ge=0)
    tags: list[str] = []

# Modelo para documento MongoDB
class Product(Document, ProductIn):
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Settings:
    name = "products" # nome da coleção