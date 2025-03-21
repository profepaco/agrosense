from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class PlantaBase(BaseModel):
    nombre: str
    especie: str

class PlantaCreate(PlantaBase):
    invernadero_id: int

class PlantaResponse(PlantaBase):
    id: int

    class Config:
        from_attributes = True

