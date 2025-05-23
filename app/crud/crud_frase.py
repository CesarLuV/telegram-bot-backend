from random import randint

from sqlalchemy import func
from sqlalchemy.orm import Session
from typing import List

from app.models.frase import Frase
from app.schemas.frase import FraseCreate


def get_all_frases_db(db: Session) -> List[Frase]:
    return db.query(Frase).all()


def get_frase(db: Session, frase_id: int):
    return db.query(Frase).filter(Frase.id == frase_id).first()


def get_random_frase(db: Session):
    return db.query(Frase).order_by(func.rand()).first()  # MySQL usa RAND()


def create_frase(db: Session, frase: FraseCreate):
    db_frase = Frase(**frase.model_dump())
    db.add(db_frase)
    db.commit()
    db.refresh(db_frase)
    return db_frase
