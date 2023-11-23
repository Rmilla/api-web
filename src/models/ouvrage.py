from typing import Optional
from datetime import datetime
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

class Ouvrage:
    __tablename__ = "ouvrage"
    id_ouvrage: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    titre_ouvrage: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    auteur_ouvrage : Mapped[str] = mapped_column(String(30))
    prix: Mapped[int] = mapped_column(int)
    isbn_ouvrage: Mapped[str] = mapped_column(str(20)) #VARCHAR(20),
    langue_ouvrage: Mapped[str] = mapped_column(str(20)) #VARCHAR(20),
    prix_ouvrage: Mapped[float] = mapped_column(float(10,2)) #DECIMAL(10, 2),
    date_parution_ouvrage: Mapped[datetime] = mapped_column(datetime) #DATE,
    categorie_ouvrage: Mapped[str] = mapped_column(str(255)) #VARCHAR(255),
    date_disponibilite_libraire_ouvrage: Mapped[datetime] = mapped_column(datetime) #DATE,
    date_disponibilite_particulier_ouvrage: Mapped[datetime] = mapped_column(datetime) #DATE,
    image_ouvrage: Mapped[str] = mapped_column(String(255)) #VARCHAR(255),
    table_des_matieres_ouvrage: Mapped[str] = mapped_column(String) #TEXT,
    mot_cle_ouvrage: Mapped[str] = mapped_column(String) #TEXT,
    description_ouvrage: Mapped[str] = mapped_column(String) #TEXT