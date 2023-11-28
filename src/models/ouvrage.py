#from typing import Optional
#from datetime import datetime
from sqlalchemy import String, Numeric, DECIMAL
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base

class Ouvrage(Base):
    __tablename__ = "ouvrage"
    id_ouvrage: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    titre_ouvrage: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    auteur_ouvrage : Mapped[str] = mapped_column(String(30))
    isbn_ouvrage: Mapped[str] = mapped_column(String(20)) #VARCHAR(20),
    langue_ouvrage: Mapped[str] = mapped_column(String(20)) #VARCHAR(20),
    prix_ouvrage: Mapped[DECIMAL] = mapped_column(Numeric(precision=10, scale=2)) #DECIMAL(10, 2),
    date_parution_ouvrage: Mapped[str] = mapped_column(String(255)) #changer en format DATE,
    categorie_ouvrage: Mapped[str] = mapped_column(String(255)) #VARCHAR(255),
    date_disponibilite_libraire_ouvrage: Mapped[str] = mapped_column(String(255)) #DATE,
    date_disponibilite_particulier_ouvrage: Mapped[str] = mapped_column(String(255)) #changer en format DATE,
    image_ouvrage: Mapped[str] = mapped_column(String(255)) #VARCHAR(255),
    table_des_matieres_ouvrage: Mapped[str] = mapped_column(String(255)) #TEXT,
    mot_cle_ouvrage: Mapped[str] = mapped_column(String(255)) #TEXT,
    description_ouvrage: Mapped[str] = mapped_column(String(255)) #TEXT


