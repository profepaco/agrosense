from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.api.schemas.lectura import LecturaCreate, LecturaResponse
from app.api.crud import lectura as crud

router = APIRouter(prefix="/lecturas", tags=["lecturas"])

@router.post("/", response_model=LecturaResponse)
def create_lectura_route(lectura: LecturaCreate, db: Session = Depends(get_db)):
    return crud.create_lectura(db, lectura)

@router.get("/{lectura_id}", response_model=LecturaResponse)
def read_lectura(lectura_id: int, db: Session = Depends(get_db)):
    db_lectura = crud.get_lectura(db, lectura_id)
    if db_lectura is None:
        raise HTTPException(status_code=404, detail="lectura no encontrado")
    return db_lectura

@router.get("/", response_model=list[LecturaResponse])
def read_lecturas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_lecturas(db, skip=skip, limit=limit)

@router.put("/{lectura_id}", response_model=LecturaResponse)
def update_lectura_route(lectura_id: int, lectura: LecturaCreate, db: Session = Depends(get_db)):
    return crud.update_lectura(db, lectura_id, lectura)

@router.delete("/{lectura_id}")
def delete_lectura_route(lectura_id: int, db: Session = Depends(get_db)):
    return crud.delete_lectura(db, lectura_id)