from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker
from src.models.base import Base
from src.models.ouvrage import Ouvrage

# connexion à la base de donnée
connector = "mysql+pymysql"
user = "root"
password = "root"
host = "localhost"
database = "librairie"

engine = create_engine(f"{connector}://{user}:{password}@{host}/{database}")
conn = sessionmaker(bind=engine)

# créer les tables
Base.metadata.create_all(engine)

async def get_db() -> Session:
    session = conn()
    try:
        yield session
    finally:
        session.close()
        