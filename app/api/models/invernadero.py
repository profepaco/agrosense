from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Invernadero(Base):
    __tablename__ = "invernaderos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)
    ubicacion = Column(String)

    plantas = relationship("Planta", back_populates="invernadero")
    sensores = relationship("Sensor", back_populates="invernadero")