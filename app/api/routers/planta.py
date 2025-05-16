from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.api.schemas.planta import PlantaCreate, PlantaResponse
from app.api.crud import planta as crud

router = APIRouter(prefix="/plantas", tags=["plantas"])

@router.post("/", response_model=PlantaResponse)
def create_planta_route(planta: PlantaCreate, db: Session = Depends(get_db)):
    return crud.create_planta(db, planta)

@router.get("/{planta_id}", response_model=PlantaResponse)
def read_planta(planta_id: int, db: Session = Depends(get_db)):
    db_planta = crud.get_planta(db, planta_id)
    if db_planta is None:
        raise HTTPException(status_code=404, detail="planta no encontrada")
    return db_planta

@router.get("/", response_model=list[PlantaResponse])
def read_plantas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_plantas(db, skip=skip, limit=limit)

@router.put("/{planta_id}", response_model=PlantaResponse)
def update_planta_route(planta_id: int, planta: PlantaCreate, db: Session = Depends(get_db)):
    return crud.update_planta(db, planta_id, planta)

@router.delete("/{planta_id}")
def delete_planta_route(planta_id: int, db: Session = Depends(get_db)):
    return crud.delete_planta(db, planta_id)