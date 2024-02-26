from fastapi import FastAPI, Path, Query,APIRouter
from typing import Optional, List
from pydantic import BaseModel

### run with uvicorn main:app --reload

router = APIRouter()

users_list = []

class User(BaseModel):
    id : int 
    email : str
    is_active : bool
    name : str
    bio : Optional[str]
    age : Optional[int]

@router.get("/users", response_model=List[User])
async def get_users():
    return users_list

@router.post("/users")
async def create_user(user : User):
    users_list.append(user)
    return  "user list is updated"
    
@router.get("/users/{id}")
async def get_user(id : int = Path(..., description = "The ID of user you want to retrieve.",
                                   ge = 0),
                   q : str = Query(None, max_length = 5)
                   ):
    return {"user": users_list[id], "query": q, "email": users_list[id].email}
