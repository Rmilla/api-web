from config.base import Base
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import Session, Mapped, mapped_column
from typing import Optional


# Création du models client avec les différentes informations nécéssaires

class Client(Base):
    __tablename__ = "t_client"

    # Colonne 'id_client' : Clé primaire, de type entier.
    id_client: Mapped[int] = mapped_column(primary_key=True)
    # Colonne 'nom_client' : Nom du cgit alient, de type chaîne de caractères (max 255 caractères).
    nom_client: Mapped[str] = mapped_column(String(255))
    # Colonne 'prenom_client' : Prénom du client, de type chaîne de caractères (max 255 caractères).
    prenom_client: Mapped[str] = mapped_column(String(255))
    # Colonne 'email_client' : Email du client, de type chaîne de caractères (max 255 caractères).
    email_client: Mapped[str] = mapped_column(String(255))
    telephone_client: Mapped[Optional[str]] = mapped_column(
        String(20), nullable=True)  # Colonne 'telephone_client' : Numéro de téléphone du client, de type chaîne de caractères (max 20 caractères).
    preferences_client: Mapped[Optional[str]] = mapped_column(
        String(255), nullable=True)  # Colonne 'preferences_client' : Préférences du client, de type chaîne de caractères (max 255 caractères).
    adresse_livraison_client: Mapped[Optional[str]] = mapped_column(
        String(255), nullable=True)  # Colonne 'adresse_livraison_client' : Adresse de livraison du client, de type chaîne de caractères (max 255 caractères).
    adresse_facturation_client: Mapped[Optional[str]] = mapped_column(
        String(255), nullable=True)  # Colonne 'adresse_facturation_client' : Adresse de facturation du client, de type chaîne de caractères (max 255 caractères).
