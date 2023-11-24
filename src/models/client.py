from config.base import Base
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import Session, Mapped, mapped_column
from typing import Optional


# Création du models client avec les différentes informations nécéssaires

class Client(Base):
    __tablename__ = "t_client"

    id_client: Mapped[int] = mapped_column(primary_key=True)
    nom_client: Mapped[str] = mapped_column(String(255))
    prenom_client: Mapped[str] = mapped_column(String(255))
    email_client: Mapped[str] = mapped_column(String(255))
    telephone_client: Mapped[Optional[str]] = mapped_column(
        String(20), nullable=True)
    preferences_client: Mapped[Optional[str]] = mapped_column(
        String(255), nullable=True)
    adresse_livraison_client: Mapped[Optional[str]] = mapped_column(
        String(255), nullable=True)
    adresse_facturation_client: Mapped[Optional[str]] = mapped_column(
        String(255), nullable=True)
