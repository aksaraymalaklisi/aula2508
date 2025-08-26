from fastapi import APIRouter, HTTPException
from beanie import PydanticObjectId
from ..models import Product, ProductIn

router = APIRouter(prefix="/products", tags=["products"])

@router.post("/", response_model=Product)

async def create_product(data: ProductIn):
    doc = Product(**data.dict())
    await doc.insert()
    return doc

@router.get("/", response_model=list[Product])
async def list_products():
    return await Product.find_all().to_list()

@router.get("/{pid}", response_model=Product)
async def get_product(pid: PydanticObjectId):
    doc = await Product.get(pid)
    if not doc:
        raise HTTPException(404, "Not found")
    return doc

# (!) INCOMPLETO - PUT/:id E DELETE/:id
