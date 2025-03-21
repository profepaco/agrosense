from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Sensor(Base):
    __tablename__ = "sensores"

    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String)  # Ejemplo: temperatura, humedad, etc.
    ubicacion = Column(String)
    invernadero_id = Column(Integer, ForeignKey("invernaderos.id"))

    invernadero = relationship("Invernadero", back_populates="sensores")
    variables = relationship("Variable", back_populates="sensor")
