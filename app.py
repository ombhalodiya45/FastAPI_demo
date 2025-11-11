from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
import uuid

app = FastAPI()

# MongoDB Connection
MONGO_URL = "mongodb://localhost:27017"
client = AsyncIOMotorClient(MONGO_URL)
db = client["fastapi_db"]
collection = db["items"]

# Schema
class Item(BaseModel):
    name: str
    price: float

# Serializer
def item_serializer(item) -> dict:
    return {
        "id": item.get("id"),
        "name": item.get("name"),
        "price": item.get("price"),
    }

# CREATE
@app.post("/items/")
async def create_item(item: Item):
    item_data = item.dict()
    item_data["id"] = str(uuid.uuid4())  # Auto-generate UUID
    await collection.insert_one(item_data)
    return {"message": "Item created successfully", "data": item_serializer(item_data)}

# READ ALL
@app.get("/items/")
async def get_items():
    items = []
    async for item in collection.find():
        items.append(item_serializer(item))
    return {"count": len(items), "items": items}

# READ ONE
@app.get("/items/{item_id}")
async def get_item(item_id: str):
    item = await collection.find_one({"id": item_id})
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item_serializer(item)

# UPDATE
@app.put("/items/{item_id}")
async def update_item(item_id: str, item: Item):
    update_result = await collection.update_one(
        {"id": item_id}, {"$set": item.dict()}
    )
    if update_result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Item not found or not modified")
    updated_item = await collection.find_one({"id": item_id})
    return {"message": "Item updated successfully", "data": item_serializer(updated_item)}

# DELETE
@app.delete("/items/{item_id}")
async def delete_item(item_id: str):
    delete_result = await collection.delete_one({"id": item_id})
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted successfully"}
