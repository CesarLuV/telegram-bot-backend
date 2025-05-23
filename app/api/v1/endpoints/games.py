from random import randint

from fastapi import APIRouter


router = APIRouter()


@router.get("/tossCoin")
async def lanzar_moneda():
    return {"side": "Head" if randint(1, 2) == 1 else "Tail"}


@router.get("/rollDice")
async def lanzar_dado():
    return {"number": randint(1, 6)}
