import business.attributes_validator as v
class aventurier:
    def __init__(self, name, axis_h, axis_v, orientation,chemin, nb_tresor=0):
        self.name=v.is_valid_string(name)
        self.axis_h=v.is_valid_number(axis_h)
        self.axis_v=v.is_valid_number(axis_v)
        self.orientation=v.is_valid_orientation(orientation)
        self.chemin=v.is_valid_string(chemin)
        self.tresors=v.is_valid_number(nb_tresor)

    def move_forward(self,c,new_index_x,new_index_y):
        self.axis_v=new_index_y
        self.axis_h=new_index_x
        c.board[self.axis_v][self.axis_h]=self.display_aventurier()

    def pivot_right(self):
        if self.orientation=='S':
            self.orientation="O"
        elif self.orientation=='E':
            self.orientation="S"
        elif self.orientation=='N':
            self.orientation="E"
        elif self.orientation=='O':
            self.orientation="N"

    def pivot_left(self):
        if self.orientation=='S':
            self.orientation="E"
        elif self.orientation=='E':
            self.orientation="N"
        elif self.orientation=='N':
            self.orientation="O"
        elif self.orientation=='O':
            self.orientation="S"

    def get_tresor(self):
        self.tresors+=1
        print(f"L'aventurier {self.name} a récolté un tresor : il détient {self.tresors}")

    def display_aventurier(self):
        return f"A({self.name})".ljust(10)

    def display_index(self,index):
        return f"{index}({self.name[:1]})".ljust(10)
