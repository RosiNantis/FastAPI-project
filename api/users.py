from typing import Optional, List
from fastapi import FastAPI, Path, Query,APIRouter
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

@router.get("/userPort", response_model=List[User])
async def get_users():
    return users_list

@router.post("/userPort")
async def create_user(user : User):
    users_list.append(user)
    return  "user list is updated"
    
@router.get("/userPort/{id}")
async def get_user(id : int):
    return {"user": users_list[id]}
