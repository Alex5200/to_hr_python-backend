from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud.main import *
from app.schemas.main import *
from app.db.session import get_db

router = APIRouter()

@router.post("/", response_model=Main)
def create_main(item: MainCreate, db: Session = Depends(get_db)):
    return create_main(db=db, item=item)

@router.get("/{item_id}", response_model=Main)
def read_main(item_id: int, db: Session = Depends(get_db)):
    db_item = get_main(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Main not found")
    return db_item

@router.put("/{item_id}", response_model=Main)
def update_main(item_id: int, item: MainCreate, db: Session = Depends(get_db)):
    db_item = get_main(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Main not found")
    return update_main(db=db, db_item=db_item, item=item)

@router.delete("/{item_id}", response_model=Main)
def delete_main(item_id: int, db: Session = Depends(get_db)):
    db_item = get_main(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Main not found")
    return delete_main(db=db, item_id=item_id)

# Add more routes as needed
