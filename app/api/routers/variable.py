from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.api.schemas.variable import VariableCreate, VariableResponse
from app.api.crud import variable as crud

router = APIRouter(prefix="/variables", tags=["variables"])

@router.post("/", response_model=VariableResponse)
def create_variable_route(variable: VariableCreate, db: Session = Depends(get_db)):
    return crud.create_variable(db, variable)

@router.get("/{variable_id}", response_model=VariableResponse)
def read_variable(variable_id: int, db: Session = Depends(get_db)):
    db_variable = crud.get_variable(db, variable_id)
    if db_variable is None:
        raise HTTPException(status_code=404, detail="Variable no encontrado")
    return db_variable

@router.get("/", response_model=list[VariableResponse])
def read_variables(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_variables(db, skip=skip, limit=limit)

@router.put("/{variable_id}", response_model=VariableResponse)
def update_variable_route(variable_id: int, variable: VariableCreate, db: Session = Depends(get_db)):
    return crud.update_variable(db, variable_id, variable)

@router.delete("/{variable_id}")
def delete_variable_route(variable_id: int, db: Session = Depends(get_db)):
    return crud.delete_variable(db, variable_id)