from MySQLdb import IntegrityError
from flask import Flask, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint

from models import Utilisateur, Client, Commande, Objet, Conditionnement
from database import SessionLocal, Base, engine
from datetime import datetime

app = Flask(__name__)
app.config["DEBUG"] = True
Base.metadata.create_all(bind=engine)

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': "API des utilisateurs"})
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.before_request
def before_request():
    """
    Attache une nouvelle session de base de données à la requête avant qu'elle ne soit traitée.
    """
    request.db = SessionLocal()

@app.after_request
def after_request(response):
    """
    Ferme la session de base de données après que la requête a été traitée.

    Arguments:
        response (flask.Response): L'objet réponse à envoyer au client.

    Retourne:
        flask.Response: L'objet réponse à envoyer au client.
    """
    request.db.close()
    return response

@app.route('/utilisateurs', methods=['GET'])
def get_utilisateurs():
    """
    Obtient une liste de tous les utilisateurs.

    Retourne:
        flask.Response: Réponse JSON contenant une liste d'utilisateurs.
    """
    session = request.db
    utilisateurs = session.query(Utilisateur).all()
    return jsonify([{
        'code_utilisateur': utilisateur.code_utilisateur,
        'nom_utilisateur': utilisateur.nom_utilisateur,
        'prenom_utilisateur': utilisateur.prenom_utilisateur,
        'username': utilisateur.username,
        'couleur_fond_utilisateur': utilisateur.couleur_fond_utilisateur,
        'date_insc_utilisateur': utilisateur.date_insc_utilisateur.isoformat()
    } for utilisateur in utilisateurs])

@app.route('/utilisateurs', methods=['POST'])
def ajouter_utilisateur():
    """
    Ajoute un nouvel utilisateur.

    Retourne:
        flask.Response: Réponse JSON indiquant le succès ou l'échec de l'opération.
    """
    data = request.json
    date_insc_utilisateur = datetime.strptime(data['date_insc_utilisateur'], '%Y-%m-%dT%H:%M:%S.%fZ')
    nouveau_utilisateur = Utilisateur(
        nom_utilisateur=data['nom_utilisateur'],
        prenom_utilisateur=data['prenom_utilisateur'],
        username=data['username'],
        couleur_fond_utilisateur=data['couleur_fond_utilisateur'],
        date_insc_utilisateur=date_insc_utilisateur
    )
    session = request.db
    session.add(nouveau_utilisateur)
    session.commit()
    return jsonify({'message': 'Utilisateur ajouté avec succès'}), 201

@app.route('/clients', methods=['GET'])
def get_clients():
    """
    Obtient une liste de tous les clients.

    Retourne:
        flask.Response: Réponse JSON contenant une liste de clients.
    """
    session = request.db
    clients = session.query(Client).all()
    return jsonify([{
        'codcli': client.codcli,
        'genrecli': client.genrecli,
        'nomcli': client.nomcli,
        'prenomcli': client.prenomcli,
        'adresse1cli': client.adresse1cli,
        'adresse2cli': client.adresse2cli,
        'adresse3cli': client.adresse3cli,
        'villecli': client.villecli,
        'cdepost': client.cdepost,
        'telcli': client.telcli,
        'emailcli': client.emailcli,
    } for client in clients])

@app.route('/clients', methods=['POST'])
def ajouter_client():
    """
    Ajoute un nouveau client.

    Retourne:
        flask.Response: Réponse JSON indiquant le succès ou l'échec de l'opération.
    """
    data = request.json
    nouveau_client = Client(
        genrecli=data['genrecli'],
        nomcli=data['nomcli'],
        prenomcli=data['prenomcli'],
        adresse1cli=data['adresse1cli'],
        adresse2cli=data['adresse2cli'],
        adresse3cli=data['adresse3cli'],
        villecli=data['villecli'],
        cdepost=data['cdepost'],
        telcli=data['telcli'],
        emailcli=data['emailcli'],
    )
    session = request.db
    session.add(nouveau_client)
    session.commit()
    return jsonify({'message': 'Client ajouté avec succès'}), 201

@app.route('/commandes', methods=['GET'])
def get_commandes():
    """
    Obtient une liste de toutes les commandes.

    Retourne:
        flask.Response: Réponse JSON contenant une liste de commandes.
    """
    session = request.db
    commandes = session.query(Commande).all()
    return jsonify([{
        'codcde': commande.codcde,
        'datcde': commande.datcde.isoformat(),
        'codcli': commande.codcli,
        'timbrecli': commande.timbrecli,
        'timbrecde': commande.timbrecde,
        'nbcolis': commande.nbcolis,
        'cheqcli': commande.cheqcli,
        'idcondit': commande.idcondit,
        'cdeComt': commande.cdeComt,
        'barchive': commande.barchive,
        'bstock': commande.bstock,
        'codeobjet': commande.codeobjet,
    } for commande in commandes])

@app.route('/commandes', methods=['POST'])
def ajouter_commande():
    """
    Ajoute une nouvelle commande.

    Retourne:
        flask.Response: Réponse JSON indiquant le succès ou l'échec de l'opération.
    """
    data = request.json
    date_commande = datetime.strptime(data['datcde'], '%Y-%m-%d').date()
    nouvelle_commande = Commande(
        datcde=date_commande,
        codcli=int(data['codcli']),
        timbrecli=float(data['timbrecli']),
        timbrecde=float(data['timbrecde']),
        nbcolis=int(data['nbcolis']),
        cheqcli=float(data['cheqcli']),
        idcondit=int(data['idcondit']),
        cdeComt=data.get('cdeComt'),
        barchive=int(data['barchive']),
        bstock=int(data['bstock']),
        codeobjet=int(data['codeobjet'])
    )
    session = request.db
    session.add(nouvelle_commande)
    session.commit()
    return jsonify({'message': 'Commande ajoutée avec succès'}), 201

@app.route('/clients/<int:codcli>/commandes', methods=['GET'])
def get_commandes_par_client(codcli):
    """
    Obtient une liste de commandes pour un client spécifique.

    Arguments:
        codcli (int): Le code du client.

    Retourne:
        flask.Response: Réponse JSON contenant une liste de commandes pour le client spécifié.
    """
    session = request.db
    commandes = session.query(Commande).filter_by(codcli=codcli).all()
    if not commandes:
        return jsonify({'message': 'Aucune commande trouvée pour ce client'}), 404

    return jsonify([{
        'codcde': commande.codcde,
        'datcde': commande.datcde.isoformat(),
        'codcli': commande.codcli,
        'timbrecli': commande.timbrecli,
        'timbrecde': commande.timbrecde,
        'nbcolis': commande.nbcolis,
        'cheqcli': commande.cheqcli,
        'idcondit': commande.idcondit,
        'cdeComt': commande.cdeComt,
        'barchive': commande.barchive,
        'bstock': commande.bstock,
        'codeobjet': commande.codeobjet,
    } for commande in commandes])

@app.route('/objets', methods=['GET'])
def get_objets():
    """
    Obtient une liste de tous les objets.

    Retourne:
        flask.Response: Réponse JSON contenant une liste d'objets.
    """
    session = request.db
    objets = session.query(Objet).all()
    return jsonify([{
        'codobj': objet.codobj,
        'designation': objet.designation,
        'poidsobj': str(objet.poidsobj),
        'points': objet.points
    } for objet in objets])

@app.route('/objets', methods=['POST'])
def ajouter_objet():
    """
    Ajoute un nouvel objet.

    Retourne:
        flask.Response: Réponse JSON indiquant le succès ou l'échec de l'opération.
    """
    data = request.json
    nouveau_objet = Objet(
        designation=data.get('designation'),
        poidsobj=data.get('poidsobj', 0.0000),
        points=data.get('points', 0)
    )
    session = request.db
    session.add(nouveau_objet)
    try:
        session.commit()
        return jsonify({'message': 'Objet ajouté avec succès'}), 201
    except IntegrityError:
        session.rollback()
        return jsonify({'message': 'Erreur lors de l\'ajout de l\'objet'}), 400

@app.route('/objets/<int:codeobjet>/commandes', methods=['GET'])
def get_commandes_par_objet(codeobjet):
    """
    Obtient une liste de commandes pour un objet spécifique.

    Arguments:
        codeobjet (int): Le code de l'objet.

    Retourne:
        flask.Response: Réponse JSON contenant une liste de commandes pour l'objet spécifié.
    """
    session = request.db
    commandes = session.query(Commande).filter_by(codeobjet=codeobjet).all()
    if not commandes:
        return jsonify({'message': 'Aucune commande trouvée pour cet objet'}), 404

    return jsonify([{
        'codcde': commande.codcde,
        'datcde': commande.datcde.isoformat(),
        'codcli': commande.codcli,
        'timbrecli': commande.timbrecli,
        'timbrecde': commande.timbrecde,
        'nbcolis': commande.nbcolis,
        'cheqcli': commande.cheqcli,
        'idcondit': commande.idcondit,
        'cdeComt': commande.cdeComt,
        'barchive': commande.barchive,
        'bstock': commande.bstock,
        'codeobjet': commande.codeobjet,
    } for commande in commandes])

@app.route('/conditionnements', methods=['GET'])
def get_conditionnements():
    """
    Obtient une liste de tous les conditionnements.

    Retourne:
        flask.Response: Réponse JSON contenant une liste de conditionnements.
    """
    session = request.db
    conditionnements = session.query(Conditionnement).all()
    return jsonify([{
        'idcondit': condit.idcondit,
        'codeobjet': condit.codeobjet,
        'quantite_min': condit.quantite_min,
        'quantite_max': condit.quantite_max,
        'modele': condit.modele,
    } for condit in conditionnements])

@app.route('/conditionnements', methods=['POST'])
def ajouter_conditionnement():
    """
    Ajoute un nouveau conditionnement.

    Retourne:
        flask.Response: Réponse JSON indiquant le succès ou l'échec de l'opération.
    """
    data = request.json
    nouveau_conditionnement = Conditionnement(
        codeobjet=data['codeobjet'],
        quantite_min=data['quantite_min'],
        quantite_max=data['quantite_max'],
        modele=data['modele']
    )
    session = request.db
    session.add(nouveau_conditionnement)
    session.commit()
    return jsonify({'message': 'Conditionnement ajouté avec succès'}), 201

@app.route('/objets/<int:codeobjet>/conditionnements', methods=['GET'])
def get_conditionnements_par_objet(codeobjet):
    """
    Obtient une liste de conditionnements pour un objet spécifique.

    Arguments:
        codeobjet (int): Le code de l'objet.

    Retourne:
        flask.Response: Réponse JSON contenant une liste de conditionnements pour l'objet spécifié.
    """
    session = request.db
    conditionnements = session.query(Conditionnement).filter_by(codeobjet=codeobjet).all()
    if not conditionnements:
        return jsonify({'message': 'Aucun conditionnement trouvé pour cet objet'}), 404

    return jsonify([{
        'idcondit': condit.idcondit,
        'codeobjet': condit.codeobjet,
        'quantite_min': condit.quantite_min,
        'quantite_max': condit.quantite_max,
        'modele': condit.modele
    } for condit in conditionnements])

if __name__ == '__main__':
    app.run(debug=True)
