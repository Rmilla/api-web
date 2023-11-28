from pydantic import BaseModel
from datetime import datetime
from typing import Optional



class PartialCommentaireUpdate(BaseModel):
    auteur_commentaire: Optional[str] = None
    titre_commentaire: Optional[str] = None

class CommentaireSchema(BaseModel):
    date_publication_commentaire: datetime
    auteur_commentaire: str
    titre_commentaire: str

    class Config:
        orm_mode = True
        from_attributes = True


class CommentaireShemaIn(CommentaireSchema):
    id_client: int
    #id_ouvrage: int


class CommentaireSchemaOut(CommentaireSchema):
    id_commentaire: int
    id_client: int
