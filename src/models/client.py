from config.connexion import Base
from typing import Optional
from sqlalchemy import create_engine, ForeignKey, select, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session

class Client(Base):


    id_client INT PRIMARY KEY AUTO_INCREMENT,
    nom_client VARCHAR(255),
    prenom_client VARCHAR(255),
    email_client VARCHAR(255),
    telephone_client VARCHAR(20),
    preferences_client TEXT,
    adresse_livraison_client TEXT,
    adresse_facturation_client TEXT
