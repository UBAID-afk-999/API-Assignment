from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Ubaid's API")

fake_db = []

class Item(BaseModel):
    id: int
    name: str
    price: int
    stock: int

@app.get("/items", response_model=List[Item])
def get_all_items():
    return fake_db

@app.post("/items")
def create_item(item: Item):
    fake_db.append(item)
    return {"message": "Item added!", "item": item}

@app.delete("/items/clear-all")
def clear_all_items():
    fake_db.clear()
    return {"message": "All items have been deleted. The database is now empty."}