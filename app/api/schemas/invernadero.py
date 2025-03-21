from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class InvernaderoBase(BaseModel):
    nombre: str
    ubicacion: str

class InvernaderoCreate(InvernaderoBase):
    pass

class InvernaderoResponse(InvernaderoBase):
    id: int
    plantas: List[PlantaResponse] = []
    sensores: List[SensorResponse] = []

    class Config:
        from_attributes = True