from sqlalchemy.orm import Session
from app.api.models.sensor import Sensor
from app.api.schemas.sensor import SensorCreate

def create_sensor(db: Session, sensor: SensorCreate):
    db_sensor = Sensor(**sensor.model_dump())
    db.add(db_sensor)
    db.commit()
    db.refresh(db_sensor)
    return db_sensor

def get_sensor(db: Session, sensor_id: int):
    return db.query(Sensor).filter(Sensor.id == sensor_id).first()

def get_sensores(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Sensor).offset(skip).limit(limit).all()

def update_sensor(db: Session, sensor_id: int, sensor: SensorCreate):
    db_sensor = get_sensor(db, sensor_id)
    if db_sensor:
        for key, value in sensor.model_dump().items():
            setattr(db_sensor, key, value)
        db.commit()
        db.refresh(db_sensor)
    return db_sensor

def delete_sensor(db: Session, sensor_id: int):
    db_sensor = get_sensor(db, sensor_id)
    if db_sensor:
        db.delete(db_sensor)
        db.commit()
    return db_sensor