# coding:utf-8
import datetime


class Tournament:
    """The tournament class is characterized by the following attributes:
    the name of the tournament  : name
    the place of the tournament : place
    the date of the tournament  : date
    the number of turn          : number_turn=4 by default
    the list of round instances : round_instance_list
    a list of players           : players_list
    a time control              : time_control=["bullet", "blitz", "quick shot" ]
    a description               : description """
    matches_list = []
    players_list = []

    def __init__(self, name, place, description="", turn_number=4):
        self.name = name
        self.place = place
        self.date = datetime.date.today().strftime("%d/%m/%Y")
        self.round_instance_list = []
        self.round_index_list = []
        self.matches_index_list = []
        self.players_index_list = []
        self.description = description
        self.turn_number = turn_number
        self.time_control = ["bullet", "blitz", "coup rapide"]

    def add_player(self, player):
        self.players_list.append(player)

    def add_matches(self, match):
        self.matches_list.append(match)

    def __repr__(self):
        """Représentation de notre objet. C'est cette chaîne qui sera affichée
        quand on saisit directement le dictionnaire dans l'interpréteur, ou en
        utilisant la fonction 'repr'"""

        return "Nom du Tournoi: {}\nLieu: {}, Date: {}, \nDescription: {} \nContrôle du temps: {} \nListe de " \
               "Tour: {} \nListe de jouer: {} \nNombre de tour: {} \nliste de match: {}".format(self.name, self.place,
                                                                                                self.date,
                                                                                                self.description,
                                                                                                self.time_control,
                                                                                                self.round_instance_list
                                                                                                ,
                                                                                                self.players_index_list,
                                                                                                self.turn_number,
                                                                                                self.matches_list)


if __name__ == '__main__':
    current_tournament = Tournament("Echec", "Paris", "Tournoi de test")
    print(current_tournament)
