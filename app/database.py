import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Charge les variables du .env
load_dotenv()

# 1- ENGINE - lit DATABASE_URL et créer le tuyau de connexion
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

# 2- SESSION - espace de travail pour les opérations de base
SessionLocal = sessionmaker(bind=engine)


def init_db():
    """
    Créer toutes les tables définies dans le models.py si elles n'existent pas
    """
    # import fait ici pour éviter les imports circulaires
    from app.models import Base
    Base.metadata.create_all(bind=engine)
