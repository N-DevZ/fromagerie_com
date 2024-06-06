# __Projet Développement d’une application informatique : cas d’étude Digicheese__
## **_Réalisation d’une API backend avec Python_**  
  
### Cahier des charges :  

L’objectif du projet est de développer le backend d’une application web pour la fromagerie Digicheese. La solution doit permettre la liaison entre l’interface visuelle de l’application et le reste celle-ci en particulier ses bases de données.  
Ces bases de données doivent elles même être mise en relation selon le schéma ULM mise à disposition par Monsieur Piangerelli.  
### Outils informatique :  

Pour ce qui est de l’espace de collaboration, nous avons utilisé Github qui permet une collaboration en temps réel très fluide.  
Pour la base de données, nous avons utilisé MySql, ainsi que MariaDB et Beaver pour le stockage de celle-ci.  
Nous avons utilisé le langage de programmation python pour la rédaction des scripts.  
Enfin, pour la parti test nous nous sommes appuyés sur Katalon recorder.  

## **_Etapes :_**

### Etape 1 mise en place du Github :

Après avoir créer un dossier conforme au attente de Diginamic, on génère une clé SSH qui y est associé.
De là chaqu'un peut mettre à jour en s'y connectant via GitBash depuis son propre poste.

### Etape 2 création de la base de donnée :

Après avoir crée un espace sur Beaver depuis le terminale de commande de MariaDB, on connecte la base de données à notre projet en mentionnant son chemin dans le code python.
On utilise ensuite le script python models.py, qui une fois executé, crée sur cette espace les 4 tables correspondant à leurs classes python respectives (depuis lesquelles sont définis leurs attributs).

### Etape 3 installation et configuration des modules :

Depuis le fichiers requirements.txt, on instal l'entiereté des modules sur python. On utilise SQLALCHEMY qui un ORM faisant communiquer la BDD et le Backend.
Flask quant à lui est le framework utilisé pour interfacer différents modules (ici swagger) grace à son API.

### Etape 4 programmation des requêtes HTTP en python :

Déclaration des roots et de l'emplacement json. Création de fonction python permettant au  client de lancer des requêtes. Pour les requêtes plus spécifiques (ex: affiche la liste des commandes pour un client donné).

### Etape 5 test fonctionnel avec swagger UI : 

Test de requêtes et documentation swagger  




