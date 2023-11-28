#import os
#import sys
#
## Add the root directory of the project to sys.path
#SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
#parent_dir = "D:\Projet_API\api-web\src" 
#os.path.dirname(SCRIPT_DIR)
#sys.path.append(parent_dir)

from fastapi import APIRouter, Depends, HTTPException, status
from src.schema.ouvrage_schema import *
from typing import List
from config.connexion import get_db
from sqlalchemy.orm import Session
from src.models import Ouvrage
ouvrage_router = APIRouter()


@ouvrage_router.post("/models/ouvrage/", response_model=OuvrageResponse, status_code=201, tags=["ouvrage"])
async def create_item(ouvrage_create: OuvrageCreate, BDD_session: Session=Depends(get_db)):

    # Générez l'ID de manière fictive (en utilisant la taille actuelle du tableau + 1)
    item = Ouvrage(**ouvrage_create.dict())
    BDD_session.add(item)
    BDD_session.commit()
    return item


#affiche la base de données
@ouvrage_router.get("/models/ouvrage/", tags=["ouvrage"])
async def read_database(BDD_session: Session=Depends(get_db)):
    ouvrages = BDD_session.query(Ouvrage).all()
    return ouvrages

# #permet de rechercher un livre en utilisant son id, son nom ou son ISBN
@ouvrage_router.get("/models/ouvrage/", response_model=List[OuvrageResponse], tags=["ouvrage"])
async def read_ouvrages(titre_ouvrage: str = "", isbn_ouvrage: str = "", theme: str = "", keyword: str = "", BDD_session: Session = Depends(get_db)): 
   
   ouvrages_query = BDD_session.query(Ouvrage)
   if titre_ouvrage: 
       ouvrages_query = ouvrages_query.filter(Ouvrage.titre_ouvrage.ilike(f"%{titre_ouvrage}%"))
   if isbn_ouvrage: 
       ouvrages_query = ouvrages_query.filter(Ouvrage.isbn_ouvrage.ilike(f"%{isbn_ouvrage}%"))
   if keyword: 
       ouvrages_query = ouvrages_query.filter(Ouvrage.mot_cle_ouvrage.ilike(f"%{keyword}%"))
   else: 
       raise HTTPException(status_code=404, detail="Ce livre n'est pas dans la librairie")

#Mise a jour d'un objet
@ouvrage_router.patch("/models/ouvrage/{ouvrage_id}", response_model=OuvrageResponse, tags=["ouvrage"])
async def update_ouvrage(ouvrage_id: int, ouvrage_update: OuvrageUpdate, BDD_session: Session = Depends(get_db)):
    existing_ouvrage = BDD_session.query(Ouvrage).filter(Ouvrage.id_ouvrage == ouvrage_id).first()

    if existing_ouvrage is None:
        raise HTTPException(status_code=404, detail="Ouvrage not found")

    for field, value in ouvrage_update.dict(exclude_unset=True).items():
        setattr(existing_ouvrage, field, value)

    BDD_session.commit()
    BDD_session.refresh(existing_ouvrage)

    return existing_ouvrage
#Suppression d'un objet
@ouvrage_router.delete("/models/ouvrage/{id_ouvrage}", response_model=None, status_code=status.HTTP_200_OK, tags=["ouvrage"])
async def delete_item(ouvrage_id: int=0, BDD_session: Session = Depends(get_db)):
    existing_ouvrage = BDD_session.query(Ouvrage).filter(Ouvrage.id_ouvrage == ouvrage_id).first()
    if existing_ouvrage is None:
        raise HTTPException(status_code=404, detail="Ce livre n'est pas dans la librairie")
    BDD_session.delete(existing_ouvrage)
    BDD_session.commit()
    return {"message": "Ouvrage deleted successfully"}

