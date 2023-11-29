from fastapi import APIRouter
from . import client_router
from . import commentaire_router
from . import ouvrage_router
from . import theme_router


def get_route():
    second_router = APIRouter()
    second_router.include_router(client_router.router)
    second_router.include_router(commentaire_router.router)
    second_router.include_router(ouvrage_router.router)
    second_router.include_router(theme_router.router)
    # , prefix="/themes", tags=["themes"]

    return second_router
