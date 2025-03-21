from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Lectura(Base):
    __tablename__ = "lecturas"

    id = Column(Integer, primary_key=True, index=True)
    valor = Column(Float)
    fecha_medicion = Column(DateTime, default=datetime.utcnow)
    variable_id = Column(Integer, ForeignKey("variables.id"))

    variable = relationship("Variable", back_populates="lecturas")