from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud.admindata import *
from app.schemas.admindata import *
from app.db.session import get_db

router = APIRouter()

@router.post("/", response_model=Admindata)
def create_admindata(item: AdmindataCreate, db: Session = Depends(get_db)):
    return create_admindata(db=db, item=item)

@router.get("/{item_id}", response_model=Admindata)
def read_admindata(item_id: int, db: Session = Depends(get_db)):
    db_item = get_admindata(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Admindata not found")
    return db_item

@router.put("/{item_id}", response_model=Admindata)
def update_admindata(item_id: int, item: AdmindataCreate, db: Session = Depends(get_db)):
    db_item = get_admindata(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Admindata not found")
    return update_admindata(db=db, db_item=db_item, item=item)

@router.delete("/{item_id}", response_model=Admindata)
def delete_admindata(item_id: int, db: Session = Depends(get_db)):
    db_item = get_admindata(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Admindata not found")
    return delete_admindata(db=db, item_id=item_id)

# Add more routes as needed
