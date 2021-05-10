from business.attributes_validator import is_valid_number
class tresor:
    def __init__(self, axis_h, axis_v,nb_tresor):
        self.axis_h=axis_h
        self.axis_v=axis_v
        self.nb_tresor=nb_tresor

    def update_tresor(self):
        self.nb_tresor-=1
        if self.nb_tresor==0:
           return True

    def display_tresor(self):
        return f"T{self.nb_tresor}".ljust(10)

    def is_valid_infos(self):
        is_valid_number(self.axis_h)
        is_valid_number(self.axis_v)
        is_valid_number(self.nb_tresor)
