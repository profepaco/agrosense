from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Planta(Base):
    __tablename__ = "plantas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    especie = Column(String)
    invernadero_id = Column(Integer, ForeignKey("invernaderos.id"))

    invernadero = relationship("Invernadero", back_populates="plantas")