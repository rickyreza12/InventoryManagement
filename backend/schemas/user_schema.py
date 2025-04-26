from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str
    role: str
    outlet_id: int

class UserLogin(BaseModel):
    username: str
    password: str