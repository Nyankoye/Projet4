"""Classe des joueurs"""
# coding:utf-8


class Player:
    """Player Class is characterized by the following attributes:
     the name of the player         : player_name
     the first name of the player   : player_first_name
     the birth day of the player    : player_birth_day
     the sex of the player          : player_sex
     the player's ranking           : player_ranking """

    def __init__(self, name, first_name, birth_day, sex, ranking):
        self.player_name = name
        self.player_first_name = first_name
        self.player_birth_day = birth_day
        self.total_score = 0
        self.player_sex = sex
        self.player_ranking = ranking
        self.player_score = 0

    def __repr__(self):
        """Représentation de notre objet. C'est cette chaîne qui sera affichée
        quand on saisit directement le dictionnaire dans l'interpréteur, ou en
        utilisant la fonction 'repr'"""

        return "Player({},{},{},{},{})".format(self.player_name, self.player_first_name,
                                               self.player_birth_day, self.player_sex,
                                               self.player_ranking)


if __name__ == '__main__':
    pass
