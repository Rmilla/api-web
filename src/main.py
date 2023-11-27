from fastapi import FastAPI
from router.ouvrage_router import ouvrage_router
from models.ouvrage import Ouvrage
from schema.ouvrage_schema import OuvrageCreate, OuvrageUpdate, OuvrageResponse

app = FastAPI()

app.include_router(ouvrage_router)


