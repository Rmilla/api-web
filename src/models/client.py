from config.connexion import Base
from typing import Optional
from sqlalchemy import create_engine, ForeignKey, select, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session

class Client(Base):
    pass