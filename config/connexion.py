#import

from typing import Optional
from __init__ import engine
from sqlalchemy import create_engine, ForeignKey, select, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session

# Établir la connexion 

conn = engine.connect()

# Déclaration des Models

class Base(DeclarativeBase):
    pass


# on creer une table association_t
   
class Association(Base):
    #nom table 
    __tablename__ = "association_t"
    
    # id de personne et passeeport
    id_personne: Mapped[int] = mapped_column(ForeignKey("t_personne.id"), primary_key=True)
    id_passeport: Mapped[int] = mapped_column(ForeignKey("t_passeport.id"), primary_key=True)
    
    # association between Assocation -> passeport
    les_passeports: Mapped["Passeport"] = relationship(back_populates="personne_associations")

    # association between Assocation -> personne
    les_personnes: Mapped["Personne"] = relationship(back_populates="passeport_associations")
    
class Personne(Base):
    
    #nom table
    __tablename__ = "t_personne"
    name:Mapped[str]=mapped_column(String(30))
    
    #id de personne 
    id: Mapped[int] = mapped_column(primary_key=True)
    
    # bidirectional de personne to passeport 
    personne_to_passeport : Mapped[list["Passeport"]] = relationship(secondary="association_t", back_populates="passeport_to_personne")
    
    # association pour aller à passeport 
    passeport_associations: Mapped[list["Association"]] = relationship(back_populates="les_personnes")
    
    def __repr__(self):
        return f"<Personne {self.name}>"
    
class Passeport(Base):
    
    #nom table
    __tablename__ = "t_passeport"
    name:Mapped[str]=mapped_column(String(30))
    
    #id de personne 
    id: Mapped[int] = mapped_column(primary_key=True)
    
    # bidirectional de passeport to personne
    passeport_to_personne : Mapped[list["Personne"]] = relationship(secondary="association_t", back_populates="personne_to_passeport")
    
    # association pour aller à personne
    personne_associations: Mapped[list["Association"]] = relationship(back_populates="les_passeports")
    
    def __repr__(self):
        return f"<Passeport {self.name}>"
    

Base.metadata.create_all(engine)
    

with Session(engine) as session:
    
    # inserer des objests 
    Mai=Personne(name="Mai")
    malienne=Passeport(name="malienne")
    malienne.passeport_to_personne.append(Mai)
    
    
    session.add_all([Mai, malienne])
    session.commit()
    
    #lire les objets
    read=select(Personne)
    read1=select(Passeport)
    
    for pointeur in session.scalars(read).all():
        print(pointeur)
        
    for pointeur1 in session.scalars(read1).all():
        print(pointeur1)