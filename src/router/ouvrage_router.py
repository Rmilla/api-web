import os
import sys

# Add the root directory of the project to sys.path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
parent_dir = "D:\Projet_API\api-web\src" 
os.path.dirname(SCRIPT_DIR)
sys.path.append(parent_dir)

from fastapi import APIRouter, Depends, HTTPException, status
from src.schema.ouvrage_schema import *
from typing import List
ouvrage_router = APIRouter()

fake_db: List[OuvrageResponse] = []


@ouvrage_router.post("/models/ouvrage", response_model=OuvrageResponse, status_code=201, tags=["ouvrage"])
async def create_item(ouvrage_create: OuvrageCreate):

    # Générez l'ID de manière fictive (en utilisant la taille actuelle du tableau + 1)
    id_ouvrage = len(fake_db) + 1
    item = OuvrageResponse(id=id_ouvrage, **ouvrage_create.dict())
    fake_db.append(item)
    return item

#affiche la base de données
@ouvrage_router.get("/models/ouvrage")
async def read_database():
     return fake_db

#permet de rechercher un livre en utilisant son id, son nom ou son ISBN
@ouvrage_router.get("/models/ouvrage/{id_ouvrage}", response_model=List[OuvrageResponse], tags=["ouvrages"])
async def read_ouvrages(id_ouvrage: int, 
                     titre_ouvrage: str, 
                     isbn_ouvrage: str,
                     theme: str,
                     keyword: str | None = None):
    result = fake_db
    if titre_ouvrage: 
        result = [book for book in result if titre_ouvrage.lower() in book["titre_ouvrage"].lower()]
    if id_ouvrage: 
        result = [book for book in result if id_ouvrage.lower() in book["id_ouvrage"].lower()]
    if id_ouvrage: 
        result = [book for book in result if theme.lower() in book["theme"].lower()]
    if id_ouvrage: 
        result = [book for book in result if keyword.lower() in book["mot_cle_ouvrage"].lower()]
    if id_ouvrage: 
        result = [book for book in result if isbn_ouvrage.lower() in book["isbn_ouvrage"].lower()]
    else: 
        raise HTTPException(status_code=404, detail="Ce livre n'est pas dans la librairie")

#Mise a jour d'un objet
@ouvrage_router.patch("/models/ouvrage/", response_model=OuvrageResponse, status_code=status.HTTP_200_OK, tags=["ouvrage"])
async def patch_item(id_ouvrage: int, item_update: OuvrageUpdate):
    client_item = OuvrageResponse(id=id_ouvrage, **item_update.dict())

    for bdd_item in fake_db:
        if bdd_item.id == id_ouvrage:
            bdd_item.copy(upadte=client_item)
            return client_item
    raise HTTPException(status_code=404, detail="Ce livre n'est pas dans la librairie")

#Suppression d'un objet
@ouvrage_router.delete("/models/ouvrage/{id_ouvrage}", response_model=dict, status_code=status.HTTP_200_OK)
async def delete_item(id_ouvrage: int):
    for item in fake_db:
        if item.id == id_ouvrage:
            fake_db.remove(item)
            return {'message':'successfully deleted item'}
    raise HTTPException(status_code=404, detail="Ce livre n'est pas dans la librairie")