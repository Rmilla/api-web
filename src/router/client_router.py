from typing import List
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from models.client import Client
from schema.client_schema import ClientSchema, ClientSchemaOut
from config.connexion import get_db


router = APIRouter()


@router.get("/client/{client_id}", response_model=ClientSchema, tags=["clients"], status_code=status.HTTP_200_OK)
async def get_client(client_id: int, session: Session = Depends(get_db)):
    query = select(Client).where(Client.id_client == client_id)
    result = session.scalars(query).one()
    if result is None:
        raise HTTPException(status_code=404, detail="Client non trouvé")

    return result


@router.get("/client", response_model=List[ClientSchema], status_code=status.HTTP_200_OK)
async def get_all_client(session: Session = Depends(get_db)):
    return session.query(Client).all()


@router.post("/create_client", response_model=ClientSchemaOut, status_code=status.HTTP_201_CREATED, summary="Créer un client",)
async def post_client(client_data: ClientSchema, session: Session = Depends(get_db)):
    client_db = Client(**client_data.dict())
    session.add(client_db)
    session.commit()
    return ClientSchemaOut.from_orm(client_db)


@router.put("/update_client/{client_id}", response_model=ClientSchema, tags=["clients"])
async def update_client(client_id: int, client_data: ClientSchema, session: Session = Depends(get_db)):
    # Recherche de client avec son Id
    query = select(Client).where(Client.id_client == client_id)
    result = session.scalars(query).first()
    # Si l'id n'est pas trouvé renvoyer un message d'erreur ("404")
    if result is None:
        raise HTTPException(status_code=404, detail="Client not found")

    for key, value in client_data.dict().items():
        if value is not None:
            raise HTTPException(status_code=400, detail="Erreur modification")
    # Sauvegarder les changements dans la base de données
    session.commit()
    return result

@router.delete("/client/{client_id}", response_model=ClientSchema, tags=["clients"], status_code=status.HTTP_200_OK)
async def delete_client(client_id: int, session: Session = Depends(get_db)):
    query = select(Client).where(Client.id_client == client_id)
    result = session.scalars(query).one()
    delete_client = session.delete(result)
    if result is None:
        raise HTTPException(status_code=404, detail="Client not found")

    return result
