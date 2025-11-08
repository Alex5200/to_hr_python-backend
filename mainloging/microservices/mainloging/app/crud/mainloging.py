from sqlalchemy.orm import Session
from app.models.mainloging import *
from app.schemas.mainloging import *

def get_mainloging(db: Session, item_id: int):
    return db.query(Mainloging).filter(Mainloging.id == item_id).first()

def create_mainloging(db: Session, item: MainlogingCreate):
    db_item = Mainloging(name=item.name, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_mainloging(db: Session, db_item: Mainloging, item: MainlogingCreate):
    db_item.name = item.name
    db_item.description = item.description
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_mainloging(db: Session, item_id: int):
    db_item = db.query(Mainloging).filter(Mainloging.id == item_id).first()
    db.delete(db_item)
    db.commit()
    return db_item
