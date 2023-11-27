from .client import Client
from .commentaire import Commentaire
from .ouvrage import Ouvrage
from config.connexion import Base
from sqlalchemy import create_engine, ForeignKey, select, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session

connector = "mysql+pymysql"
user = "root"
password = "root"
host = "localhost"
database = "testAPI"

engine = create_engine(f"{connector}://{user}:{password}@{host}/{database}")