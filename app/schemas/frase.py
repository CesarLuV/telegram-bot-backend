from pydantic import BaseModel
from datetime import datetime


class FraseBase(BaseModel):
    phrase: str
    author: str
    is_sent: bool = False


class FraseCreate(FraseBase):
    pass


class Frase(FraseBase):
    id: int
    # is_sent: bool
    created_at: datetime

    class Config:
        from_attributes = True  # Compatible con SQLAlchemy (antes `orm_mode`)
