from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

from app.api.schemas.variable import VariableResponse

class SensorBase(BaseModel):
    tipo: str
    ubicacion: str

class SensorCreate(SensorBase):
    invernadero_id: int

class SensorResponse(SensorBase):
    id: int
    variables: List[VariableResponse] = []
    class Config:
        from_attributes = True
