"""Module dans lequel se trouve toutes les fonctions permettant de controler notre application"""
from operator import itemgetter
from tinydb import TinyDB
from model.tournament import Tournament
from model.player import Player
from model.match import Match
from view import view


def create_tournament():
    """ Fonction Permetant de creer un tournoi"""
    data = view.create_tournament_view()
    tournament = Tournament(data['name'], data['place'], data['description'], data['turn_number'])
    return tournament


def create_players(tournament):
    """Fonction Permetant de creer huits joueurs a un tournoi"""
    enter_player = 1
    while enter_player <= 8:
        player_list = select_players()
        selection = view.menu_create_player(player_list)
        if selection == 1:
            # ---------------------------------------------------------------------------------
            # Joueur existant
            view.print_actors(player_list)
            data = create_existing_player()
            player_db = Player(data['Nom'], data['Prenom'], data['Date de Naissance'],
                               data['Sexe'], data['Classement'])
            # add the player id to the list of tournament players_id
            tournament.players_index_list.append(data.doc_id)
            # add the player to the list of tournament players with the tournament method
            tournament.add_player(player_db)
            # ---------------------------------------------------------------------------------
        elif selection == 2:
            # ---------------------------------------------------------------------------------
            # Nouveau joueur
            data = view.create_player_view(enter_player)
            player = Player(data['name'], data['first_name'], data['birth_day'], data['sex'],
                            data['ranking'])
            # add the player to the list of tournament players with the tournament method
            tournament.add_player(player)
            # players are registered in the database
            save_player(player)
            # prendre l'identifiantiant du joueur
            for id_player in get_players_id(1):
                tournament.players_index_list.append(id_player)
            # ---------------------------------------------------------------------------------
        enter_player += 1


def create_existing_player():
    """Fonction permettant de choisir un joueur existant"""
    logic_test = True
    data = ""
    while logic_test:
        try:
            player_choice = view.select_player_view(select_players())
            data = select_players()[player_choice]
            logic_test = False
        except IndexError as error:
            view.show(error)
            continue
    return data


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


def save_player(player):
    """Fonction permettant d'enregistrer les joueurs dans la base de données"""
    # On serialise d'abord l'instance
    serialized_player = {
        'Nom': player.player_name,
        'Prenom': player.player_first_name,
        'Date de Naissance': player.player_birth_day,
        'Sexe': player.player_sex,
        'Classement': player.player_ranking
    }
    database = TinyDB('db.json')
    players_table = database.table('players')
    # players_table.truncate()
    players_table.insert(serialized_player)


def save_round(rounds_list):
    """Fonction permettant d'enregistrer les Tours dans la base de données"""
    serialized_rounds = []
    for turn in rounds_list:
        # On serialise d'abord l'instance
        serialized_round = {
            'Nom': turn.round_name,
            'Date et heure de debut': turn.start_date,
            'Date et heure de fin': turn.end_date,
            'Identifiant des match': turn.matches_index_list
        }
        serialized_rounds.append(serialized_round)
    database = TinyDB('db.json')
    rounds_table = database.table('round')
    rounds_table.insert_multiple(serialized_rounds)


def save_match(list_matches):
    """Fonction permettant d'enregistrer les match dans la base de données"""
    serialized_matches = []
    for match in list_matches:
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
    matches_table.insert_multiple(serialized_matches)


def get_players_id(player_number):
    """Fonction permettant de recuperer les identiafiants des huits derniers joueurs"""
    database = TinyDB('db.json')
    players_table = database.table('players')
    # getting the last eight players
    id_list = []
    for i in range(1, player_number + 1):
        # getting player
        data = players_table.all()[-i]
        # Obtaining a user ID
        id_list.append(data.doc_id)
    return id_list


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
    for player_id in id_list:
        # getting the players
        player = players_table.get(doc_id=player_id)
        player_list.append(player)
    return player_list


def get_round_list(tournament):
    """Fonction permettant d'obtenir la liste de tous les tours d'un tournoi"""
    database = TinyDB('db.json')
    rounds_table = database.table('round')
    # retrieving the list of identifiers of players following a tournament
    id_list = tournament['Liste des Tours']
    round_list = []
    for round_id in id_list:
        # getting the rounds
        round_db = rounds_table.get(doc_id=round_id)
        round_list.append(round_db)
    return round_list


def get_matches_list(tournament):
    """Fonction permettant d'obtenir la liste de tous les matchs d'un tournoi"""
    database = TinyDB('db.json')
    matches_table = database.table('match')
    # recuperation de la liste des match d'un un tournoi
    matches_id_list = tournament['Liste des indices des matches']
    matches_list = []
    for id_matches in matches_id_list:
        # recuperation des joueurs
        match = matches_table.get(doc_id=id_matches)
        matches_list.append(match)
    return matches_list


def matching(list_sort, turn, tournament):
    """ Cette fonction fait correspondre le joueur 1 avec le jouer 2 le joueur 3 avec
        le joueur 4, et ainsi de suite. Si le joueur 1 a déjà joué contre le joueur 2,
        elle l'associe plutôt au joueur 3.   """
    matches = 0
    while matches < 4:
        player = list_sort[0]
        for opponent in list_sort[1:]:
            current_match = Match(player, opponent)
            if current_match in tournament.matches_list:
                continue
            tournament.add_matches(current_match)
            turn.matches_list.append(current_match)
            list_sort.remove(opponent)
            list_sort.remove(player)
            break
        matches += 1


def enter_player_score(player):
    """ Fonction de permettant de saisir le score des joueurs """
    score = 2
    while score > 1 or score < 0:
        score = view.enter_player_view(player.player_first_name)
        try:
            score = float(score)
        except ValueError:
            score = 2
            view.message('erreur')
            continue
        else:
            if score < 0:
                view.message('negatif')
                continue
            if score > 1:
                view.message('superieur')
                continue
        player.total_score += score
        return score


def enter_matches_score(match_list):
    """ Fonction de permettant de saisir le score par match des joueurs"""
    for match in match_list:
        view.show("{} vs {}".format(match.player_blanc.player_first_name,
                                    match.player_black.player_first_name))
        score_blanc = enter_player_score(match.player_blanc)
        match.score_blanc = score_blanc
        score_black = enter_player_score(match.player_black)
        match.score_black = score_black


def modify_ranking(tournament):
    """Fonction permettant de modifier le classement des joueurs d'un tournoi"""
    database = TinyDB('db.json')
    # recuperation de tous les joueurs du tournoi
    players_table = database.table('players')
    list_players = get_player_list(tournament)
    # Modification du rang joueur par joueur
    for player in list_players:
        new_ranking = view.modify_ranking_view(player)
        players_table.update({'Classement': new_ranking}, doc_ids=[player.doc_id])


def update_ranking(player):
    """Fonction permettant de modifier le classement d'un joueur"""
    database = TinyDB('db.json')
    # recuperation de tous les joueurs du tournoi
    players_table = database.table('players')
    new_ranking = view.modify_ranking_view(player)
    players_table.update({'Classement': new_ranking}, doc_ids=[player.doc_id])


def select_players():
    """Fonction permetant de selectionner un joueur existant"""
    database = TinyDB('db.json')
    # recuperation de tous les joueurs de la base de données
    list_players = database.table('players').all()
    sorted(list_players, key=itemgetter('Classement'), reverse=True)
    dico_trie = sorted(list_players, key=itemgetter('Prenom', 'Nom'))
    return dico_trie


if __name__ == '__main__':
    pass
