from fastapi import FastAPI
from .router import theme_router
from ..config.connexion import create_database

app = FastAPI()

create_database()

app.include_router(theme_router.router, prefix="/themes", tags=["themes"])
