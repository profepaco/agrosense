from sqlalchemy.orm import Session
from app.api.models.lectura import Lectura
from app.api.schemas.lectura import LecturaCreate

def create_lectura(db: Session, lectura: LecturaCreate):
    db_lectura = Lectura(**lectura.model_dump())
    db.add(db_lectura)
    db.commit()
    db.refresh(db_lectura)
    return db_lectura

def get_lectura(db: Session, lectura_id: int):
    return db.query(Lectura).filter(Lectura.id == lectura_id).first()

def get_lecturas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Lectura).offset(skip).limit(limit).all()

def update_lectura(db: Session, lectura_id: int, lectura: LecturaCreate):
    db_lectura = get_lectura(db, lectura_id)
    if db_lectura:
        for key, value in lectura.model_dump().items():
            setattr(db_lectura, key, value)
        db.commit()
        db.refresh(db_lectura)
    return db_lectura

def delete_lectura(db: Session, lectura_id: int):
    db_lectura = get_lectura(db, lectura_id)
    if db_lectura:
        db.delete(db_lectura)
        db.commit()
    return db_lectura