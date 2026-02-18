# NESETED MODELS
"""
each attribute in a pydantic model has a type
and that type can also be another pydantic model
"""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Image(BaseModel):
    url: str
    name: str

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    image: Image | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
"""
we can also use pydantic models as subtypes of list,set etc.
"""
images: list[Image] | None = None
