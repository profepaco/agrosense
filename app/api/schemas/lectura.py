from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class LecturaBase(BaseModel):
    valor: float
    fecha_medicion: datetime

class LecturaCreate(LecturaBase):
    variable_id: int

class LecturaResponse(LecturaBase):
    id: int

    class Config:
        from_attributes = True