import os
import sys

# Add the root directory of the project to sys.path
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from fastapi import FastAPI
from .router import get_route
from .config import Base
from .models import Client, Commentaire
from .router import theme_router
from ..config.connexion import create_database

Base.metadata.create_all(engine)
app = FastAPI()
app.include_router(get_route())


app.include_router(ouvrage_router)

app.include_router(theme_router.router, prefix="/themes", tags=["themes"])
