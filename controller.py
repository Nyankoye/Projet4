from model.tournament import *
from model.player import *
from model.match import *
from model.round import *
import view
from operator import attrgetter
from tinydb import TinyDB


def create_tournament():
    """ Fonction Permetant de creer un tournoi"""
    data = view.create_tournament_view()
    tournament = Tournament(data['name'], data['place'], data['description'], data['turn_number'])
    return tournament


def create_players(tournament):
    """Fonction Permetant de creer huits joueurs a un tournoi"""
    enter_player = 1
    while enter_player <= 8:
        data = view.create_player_view(enter_player)
        player = Player(data['name'], data['first_name'], data['birth_day'], data['sex'], data['ranking'])
        # add the player to the list of tournament players with the tournament method
        tournament.add_player(player)
        enter_player += 1
    # players are registered in the database
    save_player(tournament.players_list)


def save_tournament(tournament):
    """Fonction permettant d'enregistrer un tournoi dans la base de données"""
    # We serialize the instance
    serialized_tournament = {
        'Tournoi': tournament.name,
        'Lieu': tournament.place,
        'Date': tournament.date,
        'Nombre de tours': tournament.turn_number,
        'Description': tournament.description,
        'Liste des Tours': tournament.round_index_list,
        'Liste indice Joueurs': tournament.players_index_list,
        'Liste des indices des matches': tournament.matches_index_list
    }
    database = TinyDB('db.json')
    tournament_table = database.table('tournaments')
    # tournament_table.truncate()  # clear the table first
    tournament_table.insert(serialized_tournament)


def save_player(list_players):
    serialized_players = []
    for player in list_players:
        # On serialise d'abord l'instance
        serialized_player = {
            'Nom': player.player_name,
            'Prenom': player.player_first_name,
            'Date de Naissance': player.player_birth_day,
            'Sexe': player.player_sex,
            'Classement': player.player_ranking
        }
        serialized_players.append(serialized_player)
    database = TinyDB('db.json')
    players_table = database.table('players')
    # players_table.truncate()
    players_table.insert_multiple(serialized_players)


def save_round(rounds_list):
    """Fonction permettant d'enregistrer les Tours dans la base de données"""
    serialized_rounds = []
    for round in rounds_list:
        # On serialise d'abord l'instance
        serialized_round = {
            'Nom': round.round_name,
            'Date et heure de debut': round.start_date,
            'Date et heure de fin': round.end_date,
            'Identifiant des match': round.matches_index_list
        }
        serialized_rounds.append(serialized_round)
    database = TinyDB('db.json')
    rounds_table = database.table('round')
    # rounds_table.truncate()
    rounds_table.insert_multiple(serialized_rounds)


def save_match(matches_list):
    """Fonction permettant d'enregistrer les match dans la base de données"""
    serialized_matches = []
    for match in matches_list:
        # On serialise d'abord l'instance
        serialized_match = {
            'Joueur 1': match.player_blanc.player_first_name,
            'Joueur 2': match.player_black.player_first_name,
            'Score Joueur 1': match.score_blanc,
            'Score Joueur 2': match.score_black
        }
        serialized_matches.append(serialized_match)
    database = TinyDB('db.json')
    matches_table = database.table('match')
    # matches_table.truncate()
    matches_table.insert_multiple(serialized_matches)


def get_players_id(player_number):
    """Fonction permettant de recuperer les identiafiants des huits derniers joueurs"""
    database = TinyDB('db.json')
    players_table = database.table('players')
    # getting the last eight players
    id = []
    for i in range(1, player_number + 1):
        # getting player
        data = players_table.all()[-i]
        # Obtaining a user ID
        id.append(data.doc_id)
    return id


def get_round_id(turn_number):
    """Fonction permettant de recuperer les identifiants des tours d'un tournoi"""
    database = TinyDB('db.json')
    rounds_table = database.table('round')
    # recuperation du nombre de tour du tournoi
    id_round = []
    for i in range(1, turn_number + 1):
        # getting round
        data = rounds_table.all()[-i]
        # Obtaining a round ID
        id_round.append(data.doc_id)
    return id_round


def get_matches_id(match_number):
    """Fonction permettant de recuperer les identifiants des des matchs d'un tours"""
    database = TinyDB('db.json')
    matches_table = database.table('match')
    # recuperation de tous les tours
    match_id_list = []
    for i in range(1, match_number + 1):
        data = matches_table.all()[-i]
        match_id_list.append(data.doc_id)
    return match_id_list


def get_tournament_list():
    """ Fonction permettant d'obtenir la liste tous les tournois"""
    database = TinyDB('db.json')
    tournament_list = database.table('tournaments').all()
    return tournament_list


def get_player_list(tournament):
    """Fonction permettant d'obtenir la liste de tous les joueurs d'un tournoi"""
    database = TinyDB('db.json')
    players_table = database.table('players')
    # retrieving the list of identifiers of players following a tournament
    id_list = tournament['Liste indice Joueurs']
    player_list = []
    for id in id_list:
        # getting the players
        player = players_table.get(doc_id=id)
        player_list.append(player)
    return player_list


def get_round_list(tournament):
    """Fonction permettant d'obtenir la liste de tous les tours d'un tournoi"""
    database = TinyDB('db.json')
    rounds_table = database.table('round')
    # retrieving the list of identifiers of players following a tournament
    id_list = tournament['Liste des Tours']
    round_list = []
    for id in id_list:
        # getting the rounds
        round_db = rounds_table.get(doc_id=id)
        round_list.append(round_db)
    return round_list


def get_matches_list(tournament):
    database = TinyDB('db.json')
    matches_table = database.table('match')
    # recuperation de la liste des match d'un un tournoi
    matches_id_list = tournament['Liste des indices des matches']
    matches_list = []
    for id in matches_id_list:
        # recuperation des joueurs
        match = matches_table.get(doc_id=id)
        matches_list.append(match)
    return matches_list


def matching(sort_list, round, tournament):
    """ Cette fonction fait correspondre le joueur 1 avec le jouer 2 le joueur 3 avec
        le joueur 4, et ainsi de suite. Si le joueur 1 a déjà joué contre le joueur 2,
        elle l'associe plutôt au joueur 3.   """
    a = 0
    for i in range(0, len(sort_list), 2):
        # On fait correspondre les joueurs
        current_match = Match(sort_list[i + a], sort_list[i + 1])
        if current_match in tournament.matches_list and i + 2 < len(sort_list):
            current_match = Match(sort_list[i + a], sort_list[i + 2])
            tournament.add_matches(current_match)
            round.matches_list.append(current_match)
            a = -1
        else:
            tournament.add_matches(current_match)
            round.matches_list.append(current_match)
            a = 0


def enter_player_score(player):
    """ Fonction de permettant de saisir le score des joueurs """
    score = 2
    while score > 1 or score < 0:
        score = view.entry("Veuillez saisir le score de {} :\n".format(player.player_first_name))
        try:
            score = float(score)
        except ValueError as v:
            score = 2
            view.show("Vous n'avez pas saisi de nombre \nErreur:", v)
            continue
        if score < 0:
            view.show("La valeur saisi est négative")
        if score > 1:
            view.show("La valeur saisi est supérieur à 1")
        player.total_score += score
        return score


def enter_matches_score(match_list):
    """ Fonction de permettant de saisir le score par match des joueurs"""

    for match in match_list:
        print("{} vs {}".format(match.player_blanc.player_first_name, match.player_black.player_first_name))
        score_blanc = enter_player_score(match.player_blanc)
        match.score_blanc = score_blanc
        score_black = enter_player_score(match.player_black)
        match.score_black = score_black


def modify_ranking(tournament):
    """Fonction permettant de modifier le classement des joueurs d'un tournoi"""
    for player in tournament.players_list:
        ranking_value = view.modify_ranking_view(player)
        player.player_ranking = ranking_value


def sort_player():
    pass


if __name__ == '__main__':
    menu = True
    while menu:
        choice = view.menu_view()
        if choice == 2:
            # affichage de tous les tournois
            tournament_list = get_tournament_list()
            view.print_tournament_list(tournament_list)
            tournament_choice = view.choose_tournament_view(tournament_list)

            if tournament_choice == "q":
                continue
            else:
                second_menu = True
                while second_menu:
                    second_choice = view.report_tournament_view()
                    if second_choice == 1:
                        # Affichage de la liste de tous les tours d'un tournoi
                        round_list = get_round_list(tournament_list[tournament_choice])
                        view.print_rounds_list(tournament_list[tournament_choice], round_list)
                    elif second_choice == 2:
                        # affichage de la liste tous les joeurs d'un tournoi
                        player_list = get_player_list(tournament_list[tournament_choice])
                        view.print_players_list(tournament_list[tournament_choice], player_list)
                    elif second_choice == 3:
                        # affichage de la liste tous les matchs d'un tournoi
                        matches_list = get_matches_list(tournament_list[tournament_choice])
                        view.print_matches_list(tournament_list[tournament_choice], matches_list)
                    else:
                        second_menu = False

        elif choice == 1:
            # Création du Tournoi
            current_tournament = create_tournament()
            # Ajout des joueurs
            create_players(current_tournament)
            # Liste des joueurs
            players_list = current_tournament.players_list

            # Déroulement d'un match
            round_number = current_tournament.turn_number
            counter = round_number - 1
            sort_list = sorted(players_list, key=attrgetter("player_ranking"))
            half_length = len(sort_list) // 2

            # premier tour
            # création d'une instance round
            view.show("Round", round_number - counter)
            current_round = Round("Round {}".format(round_number - counter))
            for k in range(len(sort_list) // 2):
                current_tournament.add_matches(Match(sort_list[k], sort_list[half_length]))
                current_round.add_matches(Match(sort_list[k], sort_list[half_length]))
                half_length += 1
            enter_matches_score(current_round.matches_list)

            # determiner la date et leur de fin du tour
            current_round.end_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            # Sauvegarde des matchs dans la base de données
            save_match(current_round.matches_list)
            matches_id_list = get_matches_id(len(current_round.matches_list))
            current_round.matches_index_list = matches_id_list

            # Ajout des identifiant des matchs au tournoi
            for match_id in matches_id_list:
                current_tournament.matches_index_list.append(match_id)

            # Ajouter les tours au tournoi
            current_tournament.round_instance_list.append(current_round)

            counter -= 1
            # les tours restant
            while round_number - counter <= round_number:
                view.show("Round", round_number - counter)
                current_round = Round("Round {}".format(round_number - counter))
                # Trie par total de point sinon par rang
                sorted(players_list, key=attrgetter("player_ranking"))
                sort_list = sorted(players_list, key=attrgetter("total_score"), reverse=True)

                # Créer les couple de jouer
                matching(sort_list, current_round, current_tournament)
                # Entrer les resultats
                enter_matches_score(current_round.matches_list)
                current_round.end_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

                # Sauvegarde des matchs dans la base de données
                save_match(current_round.matches_list)
                matches_id_list = get_matches_id(len(current_round.matches_list))
                current_round.matches_index_list = matches_id_list

                # Ajout des identifiant des matchs au tournoi
                for match_id in matches_id_list:
                    current_tournament.matches_index_list.append(match_id)
                # Ajouter les tours au tournoi
                current_tournament.round_instance_list.append(current_round)
                counter -= 1

            # Sauvegarde des round
            save_round(current_tournament.round_instance_list)

            # Ajout des identifiant des tours au tournoi
            round_id_list = get_round_id(round_number)
            for round_id in round_id_list:
                current_tournament.round_index_list.append(round_id)

            # Sauvegarde du tournoi dans la base de données
            current_tournament.players_index_list = get_players_id(len(current_tournament.players_list))
            save_tournament(current_tournament)
        else:
            menu = False
