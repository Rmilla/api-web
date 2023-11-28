from fastapi import FastAPI
from .router import get_route
from .config import Base
from .models import Client, Commentaire
from .config import engine

Base.metadata.create_all(engine)
app = FastAPI()
app.include_router(get_route())
