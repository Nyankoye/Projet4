"""Module principale dans lequel toutes les fonction sont reuinie pour faire
  fonctionner l'application de gestion des tournois  """

from operator import attrgetter
import datetime
from controller import controller
from model.match import Match
from model.round import Round
from view import view

if __name__ == '__main__':
    # ------------------------------------------------------------------------------
    # Menu principale
    FIRST_MENU = True
    while FIRST_MENU:
        FIRST_CHOICE = view.menu_principal()
        if FIRST_CHOICE == 1:
            # ------------------------------------------------------------------------------
            # Menu Gestion des tournois
            MENU = True
            while MENU:
                CHOICE = view.menu_view1()
                if CHOICE == 2:
                    # ------------------------------------------------------------------------------
                    # Menu Gestion des tournois ==> choix d'un tournoi

                    # affichage de tous les tournois
                    tournament_list = controller.get_tournament_list()
                    view.print_tournament_list(tournament_list)
                    tournament_choice = view.choose_tournament_view(tournament_list)
                    if isinstance(tournament_choice, int) and tournament_choice < len(tournament_list):
                        SECOND_MENU = True
                        while SECOND_MENU:
                            SECOND_CHOICE = view.report_tournament_view()
                            if SECOND_CHOICE == 1:
                                # Affichage de la liste de tous les tours d'un tournoi
                                round_list = controller.get_round_list(tournament_list[tournament_choice])
                                view.print_rounds_list(tournament_list[tournament_choice], round_list)
                            elif SECOND_CHOICE == 2:
                                # affichage de la liste tous les joeurs d'un tournoi
                                player_list = controller.get_player_list(tournament_list[tournament_choice])
                                view.print_players_list(tournament_list[tournament_choice], player_list)
                            elif SECOND_CHOICE == 3:
                                # affichage de la liste tous les matchs d'un tournoi
                                matches_list = controller.get_matches_list(tournament_list[tournament_choice])
                                view.print_matches_list(tournament_list[tournament_choice], matches_list)
                            elif SECOND_CHOICE == 4:
                                # modifier le rang des joueurs d'un tounoi
                                controller.modify_ranking(tournament_list[tournament_choice])
                            else:
                                SECOND_MENU = False
                    else:
                        continue
                    # ------------------------------------------------------------------------------

                elif CHOICE == 1:
                    # ------------------------------------------------------------------------------
                    # Menu Gestion des tournois ==> Création du Tournoi

                    current_tournament = controller.create_tournament()
                    # Ajout des joueurs
                    controller.create_players(current_tournament)
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
                    controller.enter_matches_score(current_round.matches_list)

                    # determiner la date et leur de fin du tour
                    current_round.end_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

                    # Sauvegarde des matchs dans la base de données
                    controller.save_match(current_round.matches_list)
                    matches_id_list = controller.get_matches_id(len(current_round.matches_list))
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
                        controller.matching(sort_list, current_round, current_tournament)
                        # Entrer les resultats
                        controller.enter_matches_score(current_round.matches_list)
                        current_round.end_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

                        # Sauvegarde des matchs dans la base de données
                        controller.save_match(current_round.matches_list)
                        matches_id_list = controller.get_matches_id(len(current_round.matches_list))
                        current_round.matches_index_list = matches_id_list

                        # Ajout des identifiant des matchs au tournoi
                        for match_id in matches_id_list:
                            current_tournament.matches_index_list.append(match_id)
                        # Ajouter les tours au tournoi
                        current_tournament.round_instance_list.append(current_round)
                        counter -= 1

                    # Sauvegarde des round
                    controller.save_round(current_tournament.round_instance_list)

                    # Ajout des identifiant des tours au tournoi
                    round_id_list = controller.get_round_id(round_number)
                    for round_id in round_id_list:
                        current_tournament.round_index_list.append(round_id)

                    # Sauvegarde du tournoi dans la base de données
                    controller.save_tournament(current_tournament)

                    # Modification du rang des joueur
                    last_tournament = controller.get_tournament_list()[-1]
                    controller.modify_ranking(last_tournament)
                else:
                    MENU = False
                # ------------------------------------------------------------------------------
            # ------------------------------------------------------------------------------
        elif FIRST_CHOICE == 2:
            # ------------------------------------------------------------------------------
            # Menu Gestion des joueur
            db_player_list = controller.select_players()
            view.print_actors(db_player_list)
            player_choice = view.menu_view2(db_player_list)
            if isinstance(player_choice, int) and player_choice < len(db_player_list):
                controller.update_ranking(db_player_list[player_choice])
            else:
                continue
            # ------------------------------------------------------------------------------
        else:
            FIRST_MENU = False
    # ------------------------------------------------------------------------------
