from pydantic import BaseModel
from decimal import Decimal

class OuvrageCreate(BaseModel):
    titre_ouvrage: str
    auteur_ouvrage : str
    isbn_ouvrage: str
    langue_ouvrage: str
    prix_ouvrage: Decimal
    date_parution_ouvrage: str
    categorie_ouvrage: str
    date_disponibilite_libraire_ouvrage: str
    date_disponibilite_particulier_ouvrage: str
    image_ouvrage: str 
    table_des_matieres_ouvrage: str 
    mot_cle_ouvrage: str
    description_ouvrage: str

class OuvrageUpdate(BaseModel):
    titre_ouvrage: str
    auteur_ouvrage : str
    isbn_ouvrage: str
    langue_ouvrage: str
    prix_ouvrage: Decimal
    date_parution_ouvrage: str
    categorie_ouvrage: str
    date_disponibilite_libraire_ouvrage: str
    date_disponibilite_particulier_ouvrage: str
    image_ouvrage: str 
    table_des_matieres_ouvrage: str 
    mot_cle_ouvrage: str
    description_ouvrage: str

class OuvrageResponse(BaseModel):
    id_ouvrage: int
    titre_ouvrage: str
    auteur_ouvrage : str
    isbn_ouvrage: str
    langue_ouvrage: str
    prix_ouvrage: Decimal
    date_parution_ouvrage: str
    categorie_ouvrage: str
    date_disponibilite_libraire_ouvrage: str
    date_disponibilite_particulier_ouvrage: str
    image_ouvrage: str 
    table_des_matieres_ouvrage: str 
    mot_cle_ouvrage: str
    description_ouvrage: str