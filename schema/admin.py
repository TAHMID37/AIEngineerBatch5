import datetime
from pydantic import BaseModel


class Admin(BaseModel):
    id: int
    name: str
    email: str
    password: str
    created_at: datetime
    updated_at: datetime