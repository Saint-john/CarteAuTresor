import re
from model.Display import display_mountain, display_plain


class tour:
    def __init__(self, aventuriers):
        self.tour=0
        self.aventuriers=aventuriers
        if not self.aventuriers:
            raise ValueError("il n'y pas de participant, la simulation ne peut se faire.")

    def perfom_actions(self,carte,fin):
        self.tour+=1
        index=self.tour-1
        print(f"actions du tour {self.tour}")
        try:
            index
        except IndexError:
            return
        for a in self.aventuriers:
            if index < len(a.chemin):
                if a.chemin[index]=="A":
                    print(f"action de {a.name}: avancer")
                    next_position=get_next_position(self,a,carte,index)
                    if next_position[0]==1 or next_position[0]==2:
                        update_diplay_position(carte,a.axis_h,a.axis_v)
                        a.move_forward(carte,next_position[1],next_position[2])
                elif a.chemin[index]=="G":
                    print(f"action de {a.name}: pivoter à gauche")
                    a.pivot_left()
                elif a.chemin[index]=="D":
                    print(f"action de {a.name}: pivoter à droite")
                    a.pivot_right()
                elif a.chemin[index] not in "AGD":
                    print(f"L'action de {a.name}: n'a pas pu être identifié")
            else:
                fin+=1
                print("fin:"+str(fin))

        return fin



def check_if_can_move(c,a,new_index_y,new_index_x):
        if new_index_x < 0 or new_index_y < 0:
            print(f"Le mouvement prévu de l'aventurier {a.name} n'est pas possible, l'aventurier ne peut pas sortir de la carte, une coordonnée ne peut pas être negative !")
            return
        try:
            predicted_position=c.board[new_index_y][new_index_x]

            is_T=re.findall("T",predicted_position)
            print(is_T)
            is_A=re.findall("A",predicted_position)
            print(is_T)
            if is_A:
                print(f"Le mouvement prévu de l'aventurier {a.name} n'est pas possible, un aventurier fouille déjà ce terrain !")
                return
            elif predicted_position in display_mountain():
                print(f"Le mouvement prévu de l'aventurier {a.name} n'est pas possible, vous n'êtes pas équipé pour escalader cette montagne.")
                return
            elif predicted_position in display_plain(): return 1
            elif is_T:
                a.get_tresor()
                update_tresors(c,new_index_y,new_index_x)
                return 2
            else:
                return 1
        except IndexError:
            print(f"Le mouvement prévu de l'aventurier {a.name} n'est pas possible, l'aventurier ne peut pas sortir de la carte !")

def update_tresors(c,y,x):
        to_delete=False
        for t in c.tresors:
            # test si un tresor est sur la nouvelle position pour ensuite faire la maj dessus
            if (t.axis_v,t.axis_h) == (y,x):
                to_delete=t.update_tresor()
                #suppression du tresor si il n'y a plus de tresor
                if to_delete:
                    c.tresors.remove(t)

def update_diplay_position(c,y,x):
    # test si un tresor était positionné sur la case de l'aventurier avant son déplacement si oui réaffichage du tresor
    for t in c.tresors:
            if (t.axis_v,t.axis_h) == (y,x):
                print(f"tresor:{str(t.axis_v),str(t.axis_h)}, aventurier {str(y),str(x)}")
                c.board[t.axis_v][t.axis_h]=t.display_tresor()

    # test si une montagne était positionné sur la case de l'aventurier avant son déplacement si oui réaffichage de la montagne
    for m in c.mountains:
            if (m.axis_v,m.axis_h) == (y,x):
                print(f"mountain:{str(m.axis_v),str(m.axis_h)}, aventurier {str(y),str(x)}")
                c.board[m.axis_v][m.axis_h]=display_mountain()

def get_next_position(self,a,c,index_tour):
        if a.orientation in 'S':
            new_index_y=a.axis_v+1
            new_index_x=a.axis_h

        elif a.orientation in 'E':
            new_index_y=a.axis_v
            new_index_x=a.axis_h+1

        elif a.orientation in 'N':
            new_index_y=a.axis_v-1
            new_index_x=a.axis_h

        elif a.orientation in 'O':
            new_index_y=a.axis_v
            new_index_x=a.axis_h-1
        can_move=check_if_can_move(c,a,new_index_y,new_index_x)
        if can_move == 1 or can_move==2:
            c.board[a.axis_v][a.axis_h]=a.display_index(index_tour)
        return can_move,new_index_y,new_index_x

def start_simulation(c):
    print("debut de la simulation")
    fin=0
    while fin < len(c.aventuriers):
        fin=c.tour_de_jeu.perfom_actions(c,fin)
        print(c.design_map())
    print("#Fin de la simulation")
