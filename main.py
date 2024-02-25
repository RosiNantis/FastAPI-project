from fastapi import FastAPI, Path, Query
from typing import Optional, List
from user import User

### run with uvicorn main:app --reload

description = """
My test app with fastAPI and MySQL 🚀
HEre you can manage students and courses.

## Items

You can **read items**.

## Users

You will be able to:

* **Create users** (_not implemented_).
* **Read users** (_not implemented_).
"""

app = FastAPI(
    title="GetApp",
    description=description,
    version="0.0.1",
    contact={
        "name": "Alex",
        "email": "kgo@e.com"
    },
    license_info={
        "name": "MIT"
    }
)

users_list = []

@app.get("/users", response_model=List[User])
async def get_users():
    return users_list

@app.post("/users")
async def create_user(user : User):
    users_list.append(user)
    return  "user list is updated"
    
@app.get("/users/{id}")
async def get_user(id : int = Path(..., description = "The ID of user you want to retrieve.",
                                   ge = 0),
                   q : str = Query(None, max_length = 5)
                   ):
    return {"user": users_list[id], "query": q, "email": users_list[id].email}
