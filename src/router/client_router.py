from typing import List
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from ..models import Client
from ..schema import ClientSchema, ClientSchemaOut
from ..config import get_db


router = APIRouter()

# Route pour obtenir les détails d'un client spécifique par son identifiant.
# Renvoie les données du client en utilisant le schéma ClientSchema.


@router.get("/client/{client_id}", response_model=ClientSchema, tags=["clients"], status_code=status.HTTP_200_OK)
async def get_client(client_id: int, session: Session = Depends(get_db)):
    query = select(Client).where(Client.id_client == client_id)
    result = session.scalars(query).one()
    if result is None:
        raise HTTPException(status_code=404, detail="Client non trouvé")
    return result

# Route pour obtenir la liste de tous les clients.
# Renvoie une liste de clients en utilisant le schéma ClientSchema.


@router.get("/client", response_model=List[ClientSchema], status_code=status.HTTP_200_OK)
async def get_all_client(session: Session = Depends(get_db)):
    return session.query(Client).all()

# Route pour créer un nouveau client.
# Prend les données du client en entrée et les ajoute à la base de données.


@router.post("/create_client", response_model=ClientSchemaOut, status_code=status.HTTP_201_CREATED, summary="Créer un client")
async def post_client(client_data: ClientSchema, session: Session = Depends(get_db)):
    client_db = Client(**client_data.dict())
    session.add(client_db)
    session.commit()
    return ClientSchemaOut.from_orm(client_db)

# Route pour mettre à jour les informations d'un client spécifique par son identifiant.
# Modifie les champs du client spécifié en utilisant les données fournies.


@router.put("/update_client/{client_id}", response_model=ClientSchema, tags=["clients"])
async def update_client(client_id: int, client_data: ClientSchema, session: Session = Depends(get_db)):
    query = select(Client).where(Client.id_client == client_id)
    result = session.scalars(query).first()
    if result is None:
        raise HTTPException(status_code=404, detail="Client not found")
    for key, value in client_data.dict().items():
        if value is not None:
            raise HTTPException(status_code=400, detail="Erreur modification")
    session.commit()
    return result

# Route pour supprimer un client par son identifiant.
# Supprime le client spécifié de la base de données.


@router.delete("/client/{client_id}", response_model=ClientSchema, tags=["clients"], status_code=status.HTTP_200_OK)
async def delete_client(client_id: int, session: Session = Depends(get_db)):
    query = select(Client).where(Client.id_client == client_id)
    result = session.scalars(query).one()
    delete_client = session.delete(result)
    if result is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return result
