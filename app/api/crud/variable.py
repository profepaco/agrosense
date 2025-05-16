from sqlalchemy.orm import Session
from app.api.models.variable import Variable
from app.api.schemas.variable import VariableCreate

def create_variable(db: Session, variable: VariableCreate):
    db_variable = Variable(**variable.model_dump())
    db.add(db_variable)
    db.commit()
    db.refresh(db_variable)
    return db_variable

def get_variable(db: Session, variable_id: int):
    return db.query(Variable).filter(Variable.id == variable_id).first()

def get_variables(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Variable).offset(skip).limit(limit).all()

def update_variable(db: Session, variable_id: int, variable: VariableCreate):
    db_variable = get_variable(db, variable_id)
    if db_variable:
        for key, value in variable.model_dump().items():
            setattr(db_variable, key, value)
        db.commit()
        db.refresh(db_variable)
    return db_variable

def delete_variable(db: Session, variable_id: int):
    db_variable = get_variable(db, variable_id)
    if db_variable:
        db.delete(db_variable)
        db.commit()
    return db_variable