import os
import sys

# Add the root directory of the project to sys.path
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from fastapi import FastAPI
from router.ouvrage_router import ouvrage_router
from models.ouvrage import Ouvrage
app = FastAPI()

app.include_router(ouvrage_router)


