
from sqlalchemy.orm import Session
from models.share_model import DbShare
import schemas

def get_share_by_guest_id(db: Session, guest_id: int):
    """Get a share by guest id"""
    db_share = db.query(DbShare).filter(
        DbShare.guest_id == guest_id).first()
    return db_share

def create_share(db: Session, new_share: schemas.CreateShare):
    """Create a share in the database"""
    share = DbShare(**new_share.model_dump())
    db.add(share)
    db.commit()
    db.refresh(share)
    return share

