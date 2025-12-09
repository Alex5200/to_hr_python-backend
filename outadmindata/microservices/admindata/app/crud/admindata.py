from sqlalchemy.orm import Session
from app.models.admindata import *
from app.schemas.admindata import *

def get_admindata(db: Session, item_id: int):
    return db.query(Admindata).filter(Admindata.id == item_id).first()

def create_admindata(db: Session, item: AdmindataCreate):
    db_item = Admindata(name=item.name, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_admindata(db: Session, db_item: Admindata, item: AdmindataCreate):
    db_item.name = item.name
    db_item.description = item.description
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_admindata(db: Session, item_id: int):
    db_item = db.query(Admindata).filter(Admindata.id == item_id).first()
    db.delete(db_item)
    db.commit()
    return db_item
