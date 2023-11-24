from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from config.base import Base


# connexion à la base de donnée
connector = "mysql+pymysql"
user = "root"
password = "root"
host = "localhost"
database = "Librairie"

engine = create_engine(f"{connector}://{user}:{password}@{host}/{database}")


Base.metadata.create_all(engine)

SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

# Fonction pour obtenir une session de base de données


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
