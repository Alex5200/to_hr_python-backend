from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud.mainloging import *
from app.schemas.mainloging import *
from app.db.session import get_db

router = APIRouter()

@router.post("/", response_model=Mainloging)
def create_mainloging(item: MainlogingCreate, db: Session = Depends(get_db)):
    return create_mainloging(db=db, item=item)

@router.get("/{item_id}", response_model=Mainloging)
def read_mainloging(item_id: int, db: Session = Depends(get_db)):
    db_item = get_mainloging(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Mainloging not found")
    return db_item

@router.put("/{item_id}", response_model=Mainloging)
def update_mainloging(item_id: int, item: MainlogingCreate, db: Session = Depends(get_db)):
    db_item = get_mainloging(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Mainloging not found")
    return update_mainloging(db=db, db_item=db_item, item=item)

@router.delete("/{item_id}", response_model=Mainloging)
def delete_mainloging(item_id: int, db: Session = Depends(get_db)):
    db_item = get_mainloging(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Mainloging not found")
    return delete_mainloging(db=db, item_id=item_id)

# Add more routes as needed
