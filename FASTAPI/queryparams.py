#   QUERY PARAMS
from fastapi import FastAPI
app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]
"""
http://127.0.0.1:8000/items/?skip=0&limit=10 then the query params are skip and limit,
they are initially strings from the URL but will be converted to int in the function by the python typing
"""

# DEFAULT VALUES
"""
http://127.0.0.1:8000/items/ = http://127.0.0.1:8000/items/?skip=0&limit=10
if we don't pass limit in this URL: http://127.0.0.1:8000/items/?skip=20,limit is taken as 10 by default as it is mentioned in the function
"""

# OPTIONAL PARAMETERS
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}
"""
here q is optional and if not provided in the URL, defaults to None 
"""
# QUERY PARAMS TYPE CONVERSION

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
"""
short can be True or true or on or 1 yes also
"""

# MULTIPLE PATH AND QUERY PARAMS

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

"""
http://localhost:8000/users/42/items/abc123?q=search-term&short=true

user_id = 42
item_id = "abc123"
q = "search-term"
short = True
"""

# REQUIRED QUERY PARAMS
@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item
"""
here needy should be passed, for ex: http://127.0.0.1:8000/items/foo-item, we get an error as we are not passing
the needy there
"""

@app.get("/items/{item_id}")
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: int | None = None
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item

"""
needy is required
skip is default
limit is optional
"""