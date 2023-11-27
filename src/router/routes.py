from fastapi import APIRouter
from . import client_router
from . import commentaire_router


def get_route():
    second_router = APIRouter()
    second_router.include_router(client_router.router)
    second_router.include_router(commentaire_router.router)

    return second_router
