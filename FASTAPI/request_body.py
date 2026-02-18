"""
A request body is data sent by the client(let's say some browser) to our API. 
A response body is the data our API sends to the client.
Our API has to send the response body but client may not send request body all the time,
instead they can just request a path
"""

from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel): # Item is our data model
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    return item
"""
by using pydantic, we can get the associated attributes and other things with the parameter
"""
# USING THE MODEL

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.model_dump()
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

# REQUEST BODY + PATH PARAMS

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.model_dump()}

# REQUEST BODY + PATH PARAMS + QUERY PARAMS

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q": q})
    return result