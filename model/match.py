"""Classe des Matchs
    """


# coding:utf-8


class Match:
    """ Match class is characterized by the following attributes:
    the players: player_match
    the score  : player_score """

    def __init__(self, player_blanc, player_black):
        self.player_blanc = player_blanc
        self.player_black = player_black
        self.score_blanc = 0
        self.score_black = 0

    def __repr__(self):
        """Représentation de notre objet. C'est cette chaîne qui sera affichée
        quand on saisit directement le dictionnaire dans l'interpréteur, ou en
        utilisant la fonction 'repr'"""
        return "Match({},{},({}-{}))".format(self.player_blanc.player_first_name,
                                             self.player_black.player_first_name,
                                             self.score_blanc, self.score_black)

    def __eq__(self, other):
        return (self.player_blanc == other.player_blanc) and (self.player_black == other.player_black) \
               or (self.player_black == other.player_blanc) and (self.player_blanc == other.player_black)


if __name__ == '__main__':
    pass
