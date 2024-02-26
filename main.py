from fastapi import FastAPI, Path, Query
from typing import Optional, List
from api import users

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

app = FastAPI() 
app.include_router(users.router)
