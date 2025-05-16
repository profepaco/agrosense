from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

from app.api.schemas.lectura import LecturaResponse

class VariableBase(BaseModel):
    nombre: str
    unidad: str

class VariableCreate(VariableBase):
    sensor_id: int

class VariableResponse(VariableBase):
    id: int
    lecturas: List[LecturaResponse] = []

    class Config:
        from_attributes = True
