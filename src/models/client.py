# from config.base import Base
from ..config import Base
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import Session, Mapped, mapped_column, relationship
from typing import Optional


# Création du models client avec les différentes informations nécéssaires
