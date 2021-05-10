import business.attributes_validator as v
from model.Display import display_plain


class carte:
    def __init__(self, nb_case_largeur, nb_case_longueur):
        self.largeur = v.is_valid_width(nb_case_largeur)
        self.longueur = v.is_valid_length(nb_case_longueur)
        self.board = [[display_plain() for x in range(self.largeur)] for y in range(self.longueur)]
        self.mountains = []
        self.tresors = []
        self.aventuriers = []

    def design_map(self):
        for i in self.board:
            # print(" ___ "*self.largeur)
            print(" ".join(i))
            # print(" --- "*self.largeur)

    def validate_infos(self):
        v.is_valid_width(self.largeur)
        v.is_valid_length(self.longueur)


