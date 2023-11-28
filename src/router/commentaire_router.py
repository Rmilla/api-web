from typing import List
from fastapi import APIRouter
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from ..models import Commentaire
from ..schema import CommentaireSchema, CommentaireSchemaOut ,CommentaireShemaIn , PartialCommentaireUpdate
from ..config import get_db


router = APIRouter()


# Route pour récupérer tous les commentaires.
# Elle renvoie une liste de commentaires en utilisant le schéma CommentaireSchema.
@router.get("/commentaire", response_model=List[CommentaireSchema],tags=["commentaire"], status_code=status.HTTP_200_OK)
async def get_all_commentaire(session: Session = Depends(get_db)):
    return session.query(Commentaire).all()

# Route pour récupérer un commentaire spécifique par son ID.
# Elle renvoie un commentaire unique qui correspond à l'ID fourni.


@router.get("/commentaire/{commentaire_id}", tags=["commentaire"],response_model=CommentaireSchema, status_code=status.HTTP_200_OK)
async def get_commentaire(commentaire_id: int, session: Session = Depends(get_db)):
    query = select(Commentaire).where(
        Commentaire.id_commentaire == commentaire_id)
    result = session.scalars(query).one()
    if result is None:
        raise HTTPException(status_code=404, detail="Commentaire non trouvé")
    return result

# Route pour créer un nouveau commentaire.
# Elle prend en entrée les données du commentaire et les ajoute à la base de données.


@router.post("/create_commentaire", response_model=(CommentaireShemaIn), tags=["commentaire"],status_code=status.HTTP_201_CREATED)
async def create_commentaire(commentaire_data: CommentaireShemaIn, session: Session = Depends(get_db)):
    commenatire_db = Commentaire(**commentaire_data.dict())
    session.add(commenatire_db)
    session.commit()
    if commenatire_db is None:
        raise HTTPException(status_code=400, detail="Bad request")
    return CommentaireSchemaOut.from_orm(commenatire_db)

# Route pour supprimer un commentaire par son ID.
# Elle supprime le commentaire spécifié de la base de données.


@router.delete("/commentaire_delete/{commentaire_id}", response_model=(CommentaireSchema),tags=["commentaire"], status_code=status.HTTP_200_OK)
async def delete_commentaire(commentaire_id: int, session: Session = Depends(get_db)):
    query = select(Commentaire).where(
        Commentaire.id_commentaire == commentaire_id)
    result = session.scalars(query).first()
    delete_commentaire = session.delete(result)
    if result is None:
        raise HTTPException(status_code=404, detail="Commentaire not found")
    return result

# Route pour mettre à jour un commentaire par son ID.
# Elle permet de modifier les champs du commentaire spécifié.


@router.put("/update_commentaire/{commentaire_id}", response_model=(PartialCommentaireUpdate), tags=["commentaire"],status_code=status.HTTP_200_OK)
async def update_commentaire(commentaire_id: int, commentaire_data: PartialCommentaireUpdate, session: Session = Depends(get_db)):
    query = select(Commentaire).where(
    Commentaire.id_commentaire == commentaire_id)
    result = session.scalars(query).first()
    if result is None:
        raise HTTPException(status_code=404, detail="Commentaire not found")
    for key, value in commentaire_data.dict().items():
        if value is not None:
            setattr(result, key, value)
    # Sauvegarder les changements dans la base de données
    session.commit()
    return result
