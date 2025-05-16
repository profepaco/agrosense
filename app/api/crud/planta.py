from sqlalchemy.orm import Session
from app.api.models.planta import Planta
from app.api.schemas.planta import PlantaCreate

def create_planta(db: Session, planta: PlantaCreate):
    db_planta = Planta(**planta.model_dump())
    db.add(db_planta)
    db.commit()
    db.refresh(db_planta)
    return db_planta

def get_planta(db: Session, planta_id: int):
    return db.query(Planta).filter(Planta.id == planta_id).first()

def get_plantas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Planta).offset(skip).limit(limit).all()

def update_planta(db: Session, planta_id: int, planta: PlantaCreate):
    db_planta = get_planta(db, planta_id)
    if db_planta:
        for key, value in planta.model_dump().items():
            setattr(db_planta, key, value)
        db.commit()
        db.refresh(db_planta)
    return db_planta

def delete_planta(db: Session, planta_id: int):
    db_planta = get_planta(db, planta_id)
    if db_planta:
        db.delete(db_planta)
        db.commit()
    return db_planta