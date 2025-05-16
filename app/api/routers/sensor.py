from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.api.schemas.sensor import SensorCreate, SensorResponse
from app.api.crud import sensor as crud

router = APIRouter(prefix="/sensores", tags=["sensores"])

@router.post("/", response_model=SensorResponse)
def create_sensor_route(sensor: SensorCreate, db: Session = Depends(get_db)):
    return crud.create_sensor(db, sensor)

@router.get("/{sensor_id}", response_model=SensorResponse)
def read_sensor(sensor_id: int, db: Session = Depends(get_db)):
    db_sensor = crud.get_sensor(db, sensor_id)
    if db_sensor is None:
        raise HTTPException(status_code=404, detail="sensor no encontrado")
    return db_sensor

@router.get("/", response_model=list[SensorResponse])
def read_sensors(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_sensors(db, skip=skip, limit=limit)

@router.put("/{sensor_id}", response_model=SensorResponse)
def update_sensor_route(sensor_id: int, sensor: SensorCreate, db: Session = Depends(get_db)):
    return crud.update_sensor(db, sensor_id, sensor)

@router.delete("/{sensor_id}")
def delete_sensor_route(sensor_id: int, db: Session = Depends(get_db)):
    return crud.delete_sensor(db, sensor_id)