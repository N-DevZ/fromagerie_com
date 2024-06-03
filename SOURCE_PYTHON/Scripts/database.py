# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# URL de connexion à la base de données
SQLALCHEMY_DATABASE_URL = "mysql://new_user:new_password@localhost/fromagerie_com"

# Création du moteur de base de données
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Déclaration d'une base qui permet après de créer un modèle et de mapper avec SQLAlchemy
Base = declarative_base()

# Création d'une session
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
