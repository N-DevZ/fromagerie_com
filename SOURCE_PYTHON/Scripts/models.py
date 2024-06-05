# models.py
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Index, Numeric, Float
from sqlalchemy.orm import relationship
from sqlalchemy.testing.schema import Table

from database import Base

class Client(Base):
    __tablename__ = "t_client"
    codcli = Column(Integer, primary_key=True)
    genrecli = Column(String(8), default=None)
    nomcli = Column(String(40), default=None, index=True)
    prenomcli = Column(String(30), default=None)
    adresse1cli = Column(String(50), default=None)
    adresse2cli = Column(String(50), default=None)
    adresse3cli = Column(String(50), default=None)
    villecli = Column(String(50), default=None)
    cdepost = Column(Integer, default=0)
    telcli = Column(String(10), default=None)
    emailcli = Column(String(255), default=None)

class Commande(Base):
    __tablename__ = "t_entcde"
    codcde = Column(Integer, primary_key=True)
    datcde = Column(Date)
    codcli = Column(Integer, ForeignKey('t_client.codcli'))
    timbrecli = Column(Float)
    timbrecde = Column(Float)
    nbcolis = Column(Integer, default=1)
    cheqcli = Column(Float)
    idcondit = Column(Integer, default=0)
    cdeComt = Column(String(255), default=None)
    barchive = Column(Integer, default=0)
    bstock = Column(Integer, default=0)
    codeobjet = Column(Integer, ForeignKey('t_objets.codobj'))
    __table_args__ = (Index('commmande_index', "cdeComt", "codcli"),)
class Objet(Base):
    __tablename__ = "t_objets"
    codobj = Column(Integer, primary_key=True)
    designation = Column(String(50), default=None)
    poidsobj = Column(Numeric, default=0.0000)
    points = Column(Integer, default=0)

class Utilisateur(Base):
    __tablename__ = "t_utilisateur"
    code_utilisateur = Column(Integer, primary_key=True)
    nom_utilisateur = Column(String(50), default=None)
    prenom_utilisateur = Column(String(50), default=None)
    username = Column(String(50), default=None)
    couleur_fond_utilisateur = Column(Integer, default=0)
    date_insc_utilisateur = Column(Date)

class Conditionnement(Base):
    __tablename__ = "t_condits"
    idcondit = Column(Integer, primary_key=True)
    codeobjet = Column(Integer, ForeignKey('t_objets.codobj'))
    quantite_min = Column(Integer)
    quantite_max = Column(Integer)
    modele = Column(String(50))
