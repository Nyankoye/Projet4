# coding:utf-8
import datetime


class Round:
    """ Round class is characterized by the following attributes:
     the list of matches: matches_list
     the name of the round: round_name
     start date and time: start_date
     end date and time: end_date
     this class is filled automatically when a tour is created """

    def __init__(self, name):
        self.matches_list = []
        self.matches_index_list = []
        self.round_name = name
        self.start_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.end_date = 0

    def add_matches(self, match):
        self.matches_list.append(match)

    def __repr__(self):
        """Représentation de notre objet. C'est cette chaîne qui sera affichée
        quand on saisit directement le dictionnaire dans l'interpréteur, ou en
        utilisant la fonction 'repr'"""

        return "{},{},{},{},{}".format(self.matches_list, self.matches_index_list, self.round_name, self.start_date,
                                    self.end_date)


if __name__ == '__main__':
    current_round = Round("Round 1")
    print(current_round)
