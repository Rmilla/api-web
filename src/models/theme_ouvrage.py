from ..config import Base
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import Session, Mapped, mapped_column, relationship
from typing import Optional


class ThemeOuvrage(Base):
    __tablename__ = "themes_ouvrages"

    id_ouvrage = Column(Integer, ForeignKey(
        "ouvrage.id_ouvrage"), primary_key=True)
    id_theme = Column(Integer, ForeignKey("themes.theme_id"), primary_key=True)

    theme = relationship("Theme", back_populates="ouvrages")
