from sqlalchemy.orm import Session
from app.api.models.invernadero import Invernadero
from app.api.schemas.invernadero import InvernaderoCreate

def create_invernadero(db: Session, invernadero: InvernaderoCreate):
    db_invernadero = Invernadero(**invernadero.model_dump())
    db.add(db_invernadero)
    db.commit()
    db.refresh(db_invernadero)
    return db_invernadero

def get_invernadero(db: Session, invernadero_id: int):
    return db.query(Invernadero).filter(Invernadero.id == invernadero_id).first()

def get_invernaderos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Invernadero).offset(skip).limit(limit).all()

def update_invernadero(db: Session, invernadero_id: int, invernadero: InvernaderoCreate):
    db_invernadero = get_invernadero(db, invernadero_id)
    if db_invernadero:
        for key, value in invernadero.model_dump().items():
            setattr(db_invernadero, key, value)
        db.commit()
        db.refresh(db_invernadero)
    return db_invernadero

def delete_invernadero(db: Session, invernadero_id: int):
    db_invernadero = get_invernadero(db, invernadero_id)
    if db_invernadero:
        db.delete(db_invernadero)
        db.commit()
    return db_invernadero