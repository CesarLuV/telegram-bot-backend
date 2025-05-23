from fastapi import APIRouter
from app.api.v1.endpoints import frases, games


api_router = APIRouter()
api_router.include_router(frases.router, prefix="/frases", tags=["frases"])
api_router.include_router(games.router, prefix="/juegos", tags=["juegos"])
