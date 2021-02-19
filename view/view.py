"""Modules dans lequel se trouve les focntion d'affichage de notre application"""
# coding:utf-8
from operator import itemgetter
import pandas as pd


def enter_player_view(player):
    """Fonction nous permettant de saisir le score d'un joueur"""
    score = input("Veuillez saisir le score de {} :\n".format(player))
    return score


def input_int(instruction):
    """Fonction noubligeant à entrer uniquement un nombre"""
    test = True
    number = ""
    while test:
        number = input(instruction)
        if number.isdigit():
            test = False
        else:
            print("La valeur entree est une chaine de caractere")
    return int(number)


def menu_principal():
    """Fonction permettant d'afficher le menu nous permettant de faire un choix"""
    print("--------------------------------------------------")
    print("Bienvenu".center(50))
    print("--------------------------------------------------")
    print("1. Gestion des tournois")
    print("2. Gestion des joueurs")
    print("3. Quitter")
    print("--------------------------------------------------")
    choice = input_int("Veuillez saisir votre choix:\n")
    return choice


def menu_view1():
    """Fonction permettant d'afficher le menu pour faire un choix de gestion des tournois"""
    print("--------------------------------------------------")
    print("1. Créer un tournoi")
    print("2. Afficher la liste de tous les tournois")
    print("3.Retour au menu principale")
    print("--------------------------------------------------")
    choice = input_int("Veuillez saisir votre choix:\n")
    return choice


def menu_view2(player_list):
    """Fonction permettant d'afficher le menu pour faire un choix de gestion des joueurs"""
    if len(player_list) == 0:
        print("----------------------------------------------------------------------------------")
        print("Il n'existe aucun joueur enregistrer".center(83))
        print("#. Saisir q pour se retourner:")
        print("-----------------------------------------------------------------------------------")
        choice = input()
    else:
        print("----------------------------------------------------------------------------------")
        print("#. Pour modifier le rang d'un joueur veuillez faire un choix de joueur entre 0"
              " et {}:".format(len(player_list) - 1))
        print("#. Saisir q pour se retourner:")
        print("-----------------------------------------------------------------------------------")
        choice = input("Veuillez saisir votre choix:\n")
    if choice.isdigit():
        return int(choice)
    else:
        return choice


def choose_tournament_view(tournament_list):
    """Fonction nous permettant de faire un choix de tournoi dans le but d'afficher
       la liste des joueurs"""
    if len(tournament_list) == 0:
        print("----------------------------------------------------------------------------------")
        print("Il n'existe aucun tournoi enregistrer".center(83))
        print("#. Saisir q pour se retourner:")
        print("-----------------------------------------------------------------------------------")
        choice = input()
    else:
        print("----------------------------------------------------------------------------------")
        print("#. Pour afficher  les rapports d'un tournoi veuillez choisir un tournoi entre 0"
              " et {}:".format(len(tournament_list) - 1))
        print("#. Saisir q pour se retourner:")
        print("-----------------------------------------------------------------------------------")
        choice = input("Veuillez saisir votre choix:\n")
    if choice.isdigit():
        return int(choice)
    else:
        return choice


def select_player_view(players_list):
    """Fonction permettant d'afficher la liste des joeurs existant"""
    print("----------------------------------------------------------------------------------")
    print("#. Veuillez faire un choix entre le joueur 0 et le joueur {}:".format(len(players_list) - 1))
    choice = input_int("Veuillez saisir votre choix:\n")
    return choice


def report_tournament_view():
    """Fonction nous permettant de faire un choix de tournoi dans le but d'afficher soit la
       liste des joueurs soit la liste des tours d'un tournoi"""
    print("--------------------------------------------------")
    print("1.Afficher la liste des tours du tournois ")
    print("2.Afficher la liste de tous les joueurs du tournois")
    print("3.Afficher la liste de tous les matchs du tournois")
    print("4.Modifier le rang des joueurs du tournoi")
    print("5.Retour")
    print("--------------------------------------------------")
    choice = input_int("Veuillez saisir votre choix:\n")
    return choice


def create_tournament_view():
    """ Fonction nous permettant de saisir les informations de notre tournoi"""
    name = str(input("Veuillez saisir le nom du Tournoi:\n"))
    place = str(input("Veuillez saisir le lieu du Tournoi:\n"))
    description = str(input("Veuillez saisir la description du Tournoi:\n"))
    turn_number = input_int("Veuillez saisir le nombre de tour du Tournoi:\n")
    return {"name": name, "place": place, "description": description, "turn_number": turn_number}


def menu_create_player(player_list):
    """Fonction permettant d'afficher le choix entre la creation et la selection de joueur"""
    if len(player_list) == 0:
        choice = 2
        return choice
    else:
        print("--------------------------------------------------")
        print("1. Choisir un joueur existant")
        print("2. Créer un nouveau joueur")
        print("--------------------------------------------------")
        choice = input_int("Votre choix:\n")
        return choice


def create_player_view(number):
    """Fonction Permettant de saisir les information d'un joueur"""
    print("Veuillez saisir les information du joueur {}".format(number))
    name = str(input("Nom du jouer:\n"))
    first_name = str(input("Prénom du jouer:\n"))
    birth_day = str(input("Date de naissance du jouer:\n"))
    sex = str(input("Sexe du jouer:\n"))
    ranking = input_int("Classement du jouer:\n")
    return {"name": name, "first_name": first_name, "birth_day": birth_day, "sex": sex, "ranking": ranking}


def modify_ranking_view(player):
    """Fonction permettant d'afficher le joueur à modifier"""
    ranking_value = input_int(
        "Veuillez saisir le nouveau rang de {} il était classé au rang {}:\n".format(player['Prenom'],
                                                                                     player['Classement']))
    return ranking_value


def print_actors(player_list):
    """Fonction permettant d'afficher tous les acteurs de tous tournois"""
    sorted(player_list, key=itemgetter('Classement'), reverse=True)
    dico_trie = sorted(player_list, key=itemgetter('Prenom', 'Nom'))
    print(pd.DataFrame(dico_trie))


def print_players_list(tournament, player_list):
    """ Fonction permettant d'afficher la liste de tous les joueur d'un tournoi"""
    print("Liste des joueurs du tournoi: {}".format(tournament['Tournoi']))
    print_actors(player_list)


def print_rounds_list(tournament, round_list):
    """ Fonction permettant d'afficher la liste de tous les tours d'un tournoi"""
    print("Liste des Tours du tournoi: {}".format(tournament['Tournoi']))
    # Permet d'afficher tous le contenu des tours
    pd.set_option('display.expand_frame_repr', False)
    print(pd.DataFrame(round_list))


def print_matches_list(tournament, matches_lis):
    """ Fonction permettant d'afficher la liste de tous les matchs d'un tournoi"""
    print("Liste de tous les matches du tournoi: {}".format(tournament['Tournoi']))
    # Permet d'afficher tous le contenu des tours
    pd.set_option('display.expand_frame_repr', False)
    print(pd.DataFrame(matches_lis))


def print_tournament_list(tournament_list):
    """" Fonction permettant d'afficher la liste des tournois"""
    print("--------------------------------------------------")
    print("Liste des tournois".center(50))
    print("--------------------------------------------------")
    # Permet d'afficher tous le contenu des tours
    pd.set_option('display.expand_frame_repr', False)
    print(pd.DataFrame(tournament_list))


def message(keys=""):
    """Fonction d'affichage"""
    messages = {'erreur': "Vous n'avez pas saisi de nombre",
                'superieur': "La valeur saisie est supérieur à 1",
                'negatif': "La valeur saisie est négative"}
    return print(messages[keys])


def show(test, value=""):
    """Fonction d'affichage"""
    if value == "":
        print(test)
    else:
        print(test, value)


if __name__ == '__main__':
    print(isinstance(1, int))
