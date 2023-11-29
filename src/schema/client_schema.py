from pydantic import BaseModel
from typing import Optional


class ClientSchema(BaseModel):
    nom_client: str
    prenom_client: str
    email_client: str
    telephone_client: str | None = None
    preferences_client: str | None = None
    adresse_livraison_client: str | None = None
    adresse_facturation_client: str | None = None

    class Config:
        from_attributes = True


class ClientSchemaIn(ClientSchema):
    pass


class ClientSchemaOut(ClientSchema):
    id_client: int


class PartialClientUpdate(BaseModel):
    nom_client: Optional[str] = None
    prenom_client: Optional[str] = None
    email_client: Optional[str] = None
    telephone_client: Optional[str] = None
    preferences_client: Optional[str] = None
    adresse_livraison_client: Optional[str] = None
    adresse_facturation_client: Optional[str] = None
