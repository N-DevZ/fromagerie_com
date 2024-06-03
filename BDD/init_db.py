# init_db.py
from database import engine, Base
from models import Departement, Commune, Client, Commande, Conditionnement, Objet, ObjetCond, Detail, DetailObjet, Enseigne, Poids, Vignette, Role, Utilisateur, RoleUtilisateur

# Crée toutes les tables
Base.metadata.create_all(bind=engine)

print("Tables créées avec succès dans la base de données MySQL")
