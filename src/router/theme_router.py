from typing import List
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from ..models import Theme, ThemeOuvrage
from ..schema import ThemeSchema, ThemeSchemaOut
from ..config import get_db


router = APIRouter()

# Route pour obtenir les détails d'un thème spécifique par son identifiant.
# Renvoie les données du thème en utilisant le schéma ThemeSchema.


@router.get("/theme/{theme_id}", response_model=ThemeSchema, tags=["thèmes"], status_code=status.HTTP_200_OK)
async def get_theme(id_theme: int, session: Session = Depends(get_db)):
    query = select(Theme).where(Theme.theme_id == id_theme)
    result = session.scalars(query).one()
    if result is None:
        raise HTTPException(status_code=404, detail="Thème non trouvé")
    return result

# Route pour obtenir la liste de tous les thèmes.
# Renvoie une liste de thèmes en utilisant le schéma ThemeSchema.


@router.get("/theme", response_model=List[ThemeSchema], tags=["thèmes"], status_code=status.HTTP_200_OK)
async def get_all_theme(session: Session = Depends(get_db)):
    return session.query(Theme).all()

# Route pour créer un nouveau thème.
# Prend les données du thème en entrée et les ajoute à la base de données.


@router.post("/create_theme", response_model=ThemeSchema, tags=["thèmes"], status_code=status.HTTP_201_CREATED, summary="Créer un thème")
async def post_theme(theme_data: ThemeSchemaOut, session: Session = Depends(get_db)):
    theme_db = Theme(**theme_data.dict())
    session.add(theme_db)
    session.commit()
    return ThemeSchemaOut.from_orm(theme_db)

# Route pour mettre à jour les informations d'un thème spécifique par son identifiant.
# Modifie les champs du thème spécifié en utilisant les données fournies.


@router.put("/update_theme/{theme_id}", response_model=ThemeSchema, tags=["thèmes"], status_code=status.HTTP_200_OK)
async def update_theme(id_theme: int, theme_data: ThemeSchema, session: Session = Depends(get_db)):
    query = select(Theme).where(Theme.theme_id == id_theme)
    result = session.scalars(query).first()
    if result is None:
        raise HTTPException(status_code=404, detail="Thème non trouvé")
    for key, value in theme_data.dict().items():
        if value is not None:
            setattr(result, key, value)
    session.add(result)
    session.commit()
    return result

# Route pour supprimer un thème par son identifiant.
# Supprime le thème spécifié de la base de données.


@router.delete("/delete_theme/{theme_id}", response_model=ThemeSchema, tags=["thèmes"], status_code=status.HTTP_200_OK)
async def delete_theme(id_theme: int, session: Session = Depends(get_db)):
    query = select(Theme).where(Theme.theme_id == id_theme)
    result = session.scalars(query).first()
    delete_theme = session.delete(result)
    if result is None:
        raise HTTPException(status_code=404, detail="Thème non trouvé")
    return result
