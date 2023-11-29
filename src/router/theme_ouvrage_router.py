from typing import List
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from ..models import theme, theme_ouvrage
from ..schema import ThemeOuvrageSchemaOut, PartialThemeOuvrageUpdate
from ..config import get_db


router = APIRouter()

# Route pour obtenir les détails d'une relation thème-ouvrage spécifique par ses identifiants.
# Renvoie les données de la relation thème-ouvrage en utilisant le schéma ThemeOuvrageSchemaOut.


@router.get("/theme_ouvrage/{ouvrage_id}/{theme_id}", response_model=ThemeOuvrageSchemaOut, tags=["thèmes-ouvrages"], status_code=status.HTTP_200_OK)
async def get_theme_ouvrage(ouvrage_id: int, theme_id: int, session: Session = Depends(get_db)):
    query = select(theme_ouvrage).where(
        theme_ouvrage.id_ouvrage == ouvrage_id,
        theme_ouvrage.id_theme == theme_id,
    )
    result = session.scalars(query).one()
    if result is None:
        raise HTTPException(status_code=404, detail="Relation thème-ouvrage non trouvée")
    return result
