from sqlalchemy.orm import Session
from app.models.main import *
from app.schemas.main import *

def get_main(db: Session, item_id: int):
    return db.query(Main).filter(Main.id == item_id).first()

def create_main(db: Session, item: MainCreate):
    db_item = Main(name=item.name, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_main(db: Session, db_item: Main, item: MainCreate):
    db_item.name = item.name
    db_item.description = item.description
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_main(db: Session, item_id: int):
    db_item = db.query(Main).filter(Main.id == item_id).first()
    db.delete(db_item)
    db.commit()
    return db_item
