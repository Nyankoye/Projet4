# coding:utf-8
import pandas as pd


def entry(message):
    value = input(message)
    return value


def menu_view():
    """Fonction permettant d'afficher le menu nous permettant de faire un choix"""
    print("--------------------------------------------------")
    print("Bienvenu".center(50))
    print("--------------------------------------------------")
    print("1. Créer un tournoi")
    print("2. Afficher la liste de tous les tournois")
    print("3.Quitter")
    print("--------------------------------------------------")
    choice = int(input("Veuillez saisir votre choix:\n"))
    return choice


def choose_tournament_view(tournament_list):
    """Fonction nous permettant de faire un choix de tournoi dans le but d'afficher la liste des joueurs"""
    if len(tournament_list) == 0:
        print("----------------------------------------------------------------------------------")
        print("Il n'existe aucun tournoi enregistrer".center(83))
        print("#. Saisir q pour se retourner:")
        print("-----------------------------------------------------------------------------------")
        choice = input()
    else:
        print("----------------------------------------------------------------------------------")
        print("#. Pour afficher  les rapports d'un tournoi veuillez choisir un tournoi entre 1"
              " et {}:".format(len(tournament_list)))
        print("#. Saisir q pour se retourner:")
        print("-----------------------------------------------------------------------------------")
        choice = input("Veuillez saisir votre choix:\n")
    if choice == "q":
        return choice
    else:
        return int(choice) - 1


def report_tournament_view():
    """Fonction nous permettant de faire un choix de tournoi dans le but d'afficher soit la liste des joueurs
        soit la liste des tours d'un tournoi"""
    print("--------------------------------------------------")
    print("1.Afficher la liste des tours du tournois ")
    print("2.Afficher la liste de tous les joueurs du tournois")
    print("3.Afficher la liste de tous les matchs du tournois")
    print("4.Retour au menu principale")
    print("--------------------------------------------------")
    choice = int(input("Veuillez saisir votre choix:\n"))
    return choice


def create_tournament_view():
    """ Fonction nous permettant de saisir les informations de notre tournoi"""
    name = str(input("Veuillez saisir le nom du Tournoi:\n"))
    place = str(input("Veuillez saisir le lieu du Tournoi:\n"))
    description = str(input("Veuillez saisir la description du Tournoi:\n"))
    turn_number = int(input("Veuillez saisir le nombre de tour du Tournoi:\n"))
    return {"name": name, "place": place, "description": description, "turn_number": turn_number}


def create_player_view(number):
    print("Veuillez saisir les information du joueur {}".format(number))
    name = str(input("Nom du jouer:\n"))
    first_name = str(input("Prénom du jouer:\n"))
    birth_day = str(input("Date de naissance du jouer:\n"))
    sex = str(input("Sexe du jouer:\n"))
    ranking = int(input("Classement du jouer:\n"))
    return {"name": name, "first_name": first_name, "birth_day": birth_day, "sex": sex, "ranking": ranking}


def modify_ranking_view(player):
    ranking_value = int(input("Veuiller saisir le nouveau classement de {}:\n").format(player.player_first_name))
    return ranking_value


def star_view():
    print("-------------------------------------------------")
    print("Bienvenu")
    print("-------------------------------------------------")


def show(message, value=""):
    if value == "":
        print(message)
    else:
        print(message, value)


def end_view():
    pass


def actors_list():
    pass


def print_players_list(tournament, player_list):
    """ Fonction permettant d'afficher la liste de tous les joueur d'un tournoi"""
    print("Liste des joueurs du tournoi: {}".format(tournament['Tournoi']))
    print(pd.DataFrame(player_list))


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


if __name__ == '__main__':
    pass
