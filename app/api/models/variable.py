from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Variable(Base):
    __tablename__ = "variables"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)  # Tipo de variable: Temperatura, Humedad, etc.
    unidad = Column(String)  # °C, %, ppm, etc.
    sensor_id = Column(Integer, ForeignKey("sensores.id"))

    sensor = relationship("Sensor", back_populates="variables")
    lecturas = relationship("Lectura", back_populates="variable")