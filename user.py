from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id : int 
    email : str
    is_active : bool
    name : str
    bio : Optional[str]