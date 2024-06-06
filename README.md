# __Projet Développement d’une application informatique : cas d’étude Digicheese__
## **_Réalisation d’une API backend avec Python_**  

![photo python](https://scontent-mrs2-1.xx.fbcdn.net/v/t1.15752-9/441396104_1443074782979942_75931217175817883_n.png?_nc_cat=111&ccb=1-7&_nc_sid=5f2048&_nc_ohc=8UgiHJPrdPsQ7kNvgGZSaib&_nc_ht=scontent-mrs2-1.xx&oh=03_Q7cD1QE5ikDJd3LH5OM0SA-7-dgzm8B39jQyqq6qHJHT93y9zQ&oe=6689148C) ![photo](https://scontent-mrs2-2.xx.fbcdn.net/v/t1.15752-9/441377110_474134318314164_8759843846568836743_n.png?_nc_cat=102&ccb=1-7&_nc_sid=5f2048&_nc_ohc=zJWxBXcGcUoQ7kNvgH-MLub&_nc_ht=scontent-mrs2-2.xx&oh=03_Q7cD1QGABG_r7MYbtk_q6_y7f3dLboLPdE5NlUKJ7de5JS521A&oe=66893557)
  
### Cahier des charges :  

L’objectif du projet est de développer le backend d’une application web pour la fromagerie Digicheese. La solution doit permettre la liaison entre l’interface visuelle de l’application et le reste celle-ci en particulier ses bases de données.  
Ces bases de données doivent elles même être mise en relation selon le schéma UML mise à disposition par Monsieur PIANGERELLI.  
### Outils informatique :  

Pour ce qui est de l’espace de collaboration, nous avons utilisé Github qui permet une collaboration en temps réel très fluide.  
Pour la base de données, nous avons utilisé MySql, ainsi que MariaDB et Beaver pour le stockage de celle-ci.  
Nous avons utilisé le langage de programmation python pour la rédaction des scripts.  
Enfin, pour la partie test nous nous sommes appuyés sur Katalon recorder.  

## **_Etapes :_**

### Etape 1 mise en place du Github :

Après avoir créé un dossier conforme au attente de Diginamic, on génère une clé SSH qui y est associé.
De là chaqu'un peut mettre à jour en s'y connectant via GitBash depuis son propre poste.

### Etape 2 création de la base de données :

Après avoir créé un espace sur Beaver depuis le terminale de commande de MariaDB, on connecte la base de données à notre projet en mentionnant son chemin dans le code python.
On utilise ensuite le script python models.py, qui une fois executé, crée sur cette espace les 4 tables correspondant à leurs classes python respectives (depuis lesquelles sont définis leurs attributs).

### Etape 3 installation et configuration des modules :

Depuis le fichiers requirements.txt, on instal l'entiereté des modules sur python. On utilise SQLALCHEMY qui un ORM faisant communiquer la BDD et le Backend.
Flask quant à lui est le framework utilisé pour interfacer différents modules (ici swagger) grace à son API.

![](https://scontent-mrs2-1.xx.fbcdn.net/v/t1.15752-9/441623377_1209910386853686_7741098829471154113_n.png?_nc_cat=100&ccb=1-7&_nc_sid=5f2048&_nc_ohc=P0IfmAtzbbMQ7kNvgGYf332&_nc_ht=scontent-mrs2-1.xx&oh=03_Q7cD1QGMMY-jeSSu2ftvXYIDNO8pMwCqderJsK9vH87hy9ZlZQ&oe=66893273)

### Etape 4 programmation des requêtes HTTP en python :

Déclaration des roots et de l'emplacement json. Création de fonction python permettant au  client de lancer des requêtes. Pour les requêtes plus spécifiques (ex: affiche la liste des commandes pour un client donné).

### Etape 5 test fonctionnel avec swagger UI : 

Test de requêtes et documentation swagger 

### Étape 6 test driven development avec katalina recorder: 

Création d'une suite de tests regroupant des cas de tests par requetes et par entités

### Étape 7 documentation technique avec pydoc :

Installation de pydoc et commande **python.exe -m pydoc -w app models database**
permettant de générer une documentation HTML grâce aux docstrings dans le code Python 

**_Hetiandro FERREIRA_**
**_Nathan DEVOISE_**
**_Assala SOUSSI_**
**_Antoine FONTANILLE_**


