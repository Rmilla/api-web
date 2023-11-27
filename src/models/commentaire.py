from ..config import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import Session, Mapped, mapped_column, relationship
from typing import Optional
from datetime import datetime

# Création du models Commentaire avec les différentes informations nécéssaires et les liens avec les autres tables


class Commentaire(Base):
    __tablename__ = "t_commentaire"  # nommage de la table

    id_commentaire: Mapped[int] = mapped_column(
        primary_key=True)  # Création de l'id avec sa clé primaire
    # Clé etrangère, récupérant l'id client
    id_client: Mapped[int] = mapped_column(ForeignKey("t.client.id_client"))
    # Clé etrangère, récupérant l'id ouvrage
    id_ouvrage: Mapped[int] = mapped_column(ForeignKey("t_ouvrage.id_ouvrage"))
    # Création de la date publication avec comme attribut dateTime, pour les dates
    date_publication_commentaire: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow)
    # Colonne 'auteur_commentaire' : de type chaîne de caractères (max 255 caractères).
    auteur_commentaire: Mapped[str] = mapped_column(String(255))
    # Colonne 'titre_commentaire' :  de type chaîne de caractères (max 255 caractères).
    titre_commentaire: Mapped[str] = mapped_column(String(255))

    #client = relationship("Client")
    #ouvrage = relationship("Ouvrage")
