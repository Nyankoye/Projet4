# Projet 4 Gestion de Tournoi Echecs
Ce projet s’inscrit dans le cadre de la réalisation d’une application console de gestion de tournoi d'echecs. 
L'application va permettre création d'un tournoi, l'ajout des joueurs à un tournoi et l'enregistrement des informations dans une mini base de données.
# Execution du code
 Pour exécuter ce code vous devez disposer de tous les paquets nécessaires à son exécution pour cela vous devez :
 * Téléchargez le script et le fichier requirements.txt et les placer dans un dossier vide.
 * Créez un environnement virtuel en utilisant la commandes: python -m venv env
 * Activez l'environnement virtuel en utilisant la commandes: source env/bin/activate 
 * Installer les paquets Python répertoriés dans le fichier requirements.txt en utilisant la commande : pip install -r requirements.txt
 * Pour lancer le programme utiliser la commande: python gt_echec1.py 
## Generation Fichier flake8
 Pour genener un fichier flake8 vous devez utiliser les commandes suivantes:
 * Indiquer à flake8 le nombre maximun de caractère avec la commande: flake8 --max-line-length 119 dir/
 * Puis generer le fichier avec la commande: flake8 --format=html --htmldir=flake-report
## Utlisation de l'application
 le menu principale de l'application contient trois (3) options:
 1. Gestion des tournois
 2. Gestion des joueurs
 3. Quitter
 * le choix 1 contiens les options suivantes:
 1. Créer un tournoi
 2. Afficher la liste de tous les tournois
 3. Retour au menu principale
 * Dans la seconde option de ce second menu nous aurons les options suivantes:
 1. Le choix d'un tournoi
   lorque nous choissons un tournoi nous pourrons afficher toutes les information sur le tournoi à savoir:
   1.Afficher la liste des tours du tournois 
   2.Afficher la liste de tous les joueurs du tournois
   3.Afficher la liste de tous les matchs du tournois
   4.Modifier le rang des joueurs du tournoi
 2. le retour
* le choix 2 du menu principale nous permet d'afficher la liste de tous les acteurs du tournois
* lorsque nous choississons un joueur nous pouvons modifier son rang

