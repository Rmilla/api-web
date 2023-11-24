from fastapi import FastAPI
from router import client_router, commentaire_router
from models import Client
from models import Commentaire
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from config.base import Base
from config.connexion import engine

app = FastAPI()
app.include_router(client_router.router)
app.include_router(commentaire_router.router)

'''
with Session(engine) as session:
    ClientTest = Client(nom_client="Andy", prenom_client="O", email_client="andy@hotmail.com", telephone_client="0789998998",
                        preferences_client="Horreur", adresse_livraison_client="rue de la paix", adresse_facturation_client="rue de l'amour")

    CommentaireTest = Commentaire(
        auteur_commentaire="Oui très bien", titre_commentaire="Une claque artistique")
    session.add_all([ClientTest, CommentaireTest])
    session.commit()
session.close()
'''
