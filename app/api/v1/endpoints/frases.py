from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.models.frase import Frase
from app.schemas.frase import Frase, FraseCreate
from app.crud.crud_frase import get_all_frases_db, get_frase, get_random_frase, create_frase
from app.database.session import get_db


router = APIRouter()


@router.get("/", response_model=List[Frase])
async def listar_frases(db: Session = Depends(get_db)):
    frases = get_all_frases_db(db)
    return frases


@router.get("/random", response_model=Frase)
def leer_frase_aleatoria(db: Session = Depends(get_db)):
    db_frase = get_random_frase(db)
    if db_frase is None:
        raise HTTPException(status_code=404, detail="No hay frases disponibles")
    return db_frase


@router.get("/{frase_id}", response_model=Frase)
def leer_frase(frase_id: int, db: Session = Depends(get_db)):
    db_frase = get_frase(db, frase_id=frase_id)
    if db_frase is None:
        raise HTTPException(status_code=404, detail="Frase no encontrada")
    return db_frase


@router.post("/", response_model=Frase)
def crear_frase(frase: FraseCreate, db: Session = Depends(get_db)):
    return create_frase(db=db, frase=frase)
