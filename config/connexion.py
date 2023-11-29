from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

connector = "mysql+pymysql"
user = "root"
password = "root"
host = "localhost"
database = "librairie"

engine = create_engine(f"{connector}://{user}:{password}@{host}/{database}")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Base(DeclarativeBase):
    pass

Base.metadata.create_all(bind=engine)
