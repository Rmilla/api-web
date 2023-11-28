import os
import sys
print(sys.path)
# Add the root directory of the project to sys.path
parent_dir = r"d:/Projet_API/api-web/src/"
sys.path.append(os.path.abspath(parent_dir))

from fastapi import FastAPI
from router.ouvrage_router import ouvrage_router
from models.ouvrage import Ouvrage
app = FastAPI()

app.include_router(ouvrage_router)


