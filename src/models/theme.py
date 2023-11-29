from ..config import Base
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import Session, Mapped, mapped_column, relationship
from typing import Optional

class Theme(Base):
    __tablename__ = "themes"

    theme_id = Column(Integer, primary_key=True, autoincrement=True)
    nom_theme = Column(String(255), index=True)

    ouvrages = relationship("ThemeOuvrage", back_populates="theme")
