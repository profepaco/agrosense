from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.api.schemas.invernadero import InvernaderoCreate, InvernaderoResponse
from app.api.crud import invernadero as crud

router = APIRouter(prefix="/invernaderos", tags=["Invernaderos"])

@router.post("/", response_model=InvernaderoResponse)
def create_invernadero_route(invernadero: InvernaderoCreate, db: Session = Depends(get_db)):
    return crud.create_invernadero(db, invernadero)

@router.get("/{invernadero_id}", response_model=InvernaderoResponse)
def read_invernadero(invernadero_id: int, db: Session = Depends(get_db)):
    db_invernadero = crud.get_invernadero(db, invernadero_id)
    if db_invernadero is None:
        raise HTTPException(status_code=404, detail="Invernadero no encontrado")
    return db_invernadero

@router.get("/", response_model=list[InvernaderoResponse])
def read_invernaderos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_invernaderos(db, skip=skip, limit=limit)

@router.put("/{invernadero_id}", response_model=InvernaderoResponse)
def update_invernadero_route(invernadero_id: int, invernadero: InvernaderoCreate, db: Session = Depends(get_db)):
    return crud.update_invernadero(db, invernadero_id, invernadero)

@router.delete("/{invernadero_id}")
def delete_invernadero_route(invernadero_id: int, db: Session = Depends(get_db)):
    return crud.delete_invernadero(db, invernadero_id)