from pydantic import BaseModel # BaseModel nos permite crear entidades
from typing import Optional
# Modelo de usuario. Entidad User
class User(BaseModel):  # nos da la capacidad de crear una entidad
    id: Optional[str] = None
    username: str
    email: str
