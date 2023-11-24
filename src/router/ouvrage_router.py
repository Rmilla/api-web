from fastapi import APIRouter, Depends, HTTPException, status
from models.ouvrage import *
from schema.ouvrage_schema import *


router = APIRouter()

fake_db = [[]]


@router.post("/models/ouvrage", response_model=ItemResponse, status_code=201, tags=["ouvrage"])
async def create_item(ouvrage_create: ItemCreate):
    # Générez l'ID de manière fictive (en utilisant la taille actuelle du tableau + 1)
    id_ouvrage = len(fake_db) + 1
    item = ItemResponse(id=id_ouvrage, **ouvrage_create.dict())
    fake_db.append(item)
    return item

#affiche la base de données
@router.get("/models/ouvrage")
async def read_items():
     return fake_db
#permet de rechercher un livre en utilisant son id, son nom ou son ISBN
@router.get("/models/ouvrage{id_ouvrage}/models/ouvrage/{titre_ouvrage}/models/ouvrage/{isbn_ouvrage}")
async def read_items(id_ouvrage: int, 
                     titre_ouvrage: str, 
                     isbn_ouvrage: str | None = None):
     return {"name": fake_db[id_ouvrage]["name"], "item_id": id_ouvrage}



#Mise a jour d'un objet
@router.patch("/models/ouvrage/{id_ouvrage}", response_model=ItemResponse, status_code=status.HTTP_200_OK, tags=["ouvrage"])
async def patch_item(id_ouvrage: int, item_update: ItemUpdate):
    client_item = ItemResponse(id=id_ouvrage, **item_update.dict())

    for bdd_item in fake_db:
        if bdd_item.id == id_ouvrage:
            bdd_item.copy(upadte=client_item)
            return client_item
    raise HTTPException(status_code=404, detail="Item not found")

#Suppression d'un objet
@router.delete("/models/ouvrage/{id_ouvrage}", response_model=dict, status_code=status.HTTP_200_OK)
async def delete_item(id_ouvrage: int):
    for item in fake_db:
        if item.id == id_ouvrage:
            fake_db.remove(item)
            return {'message':'successfully deleted item'}
    raise HTTPException(status_code=404, detail="Item not found")