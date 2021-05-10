from tour import tour
from carte import carte
from aventurier import aventurier
from tour import start_simulation
from tresor import tresor
from tour import update_tresors
from tour import check_if_can_move
from mountain import mountain
from carte import display_mountain
def test_simulation():
    c=carte(4,4)
    c.aventuriers.append(aventurier("john",3,2,"S","ADAGGADA"))
    c.aventuriers.append(aventurier("lucie",1,1,"N","AGGAAADAAGA"))
    c.tour_de_jeu=tour(c.aventuriers)
    start_simulation(c)
    assert c.tour_de_jeu
    assert len(c.tour_de_jeu.aventuriers) == 2

def test_delete_tresor_when_0():
    c=carte(4,4)
    c.tresors.append(tresor(3,3,1))
    c.tresors.append(tresor(1,1,2))
    update_tresors(c,y=3,x=3)
    assert len(c.tresors)==1

def test_aventurier_move_on_tresor():
    c=carte(4,4)
    m1=mountain(1,0)
    m2=mountain(3,3)
    c.mountains.append(m1)
    c.mountains.append(m2)
    c.board[m1.axis_v][m1.axis_h]=display_mountain()
    c.board[m2.axis_v][m2.axis_h]=display_mountain()
    t=tresor(2,2,1)
    c.tresors.append(t)
    c.board[t.axis_v][t.axis_h]=t.display_tresor()
    a1=aventurier("john",3,2,"S","ADAGGADA")
    a2=aventurier("lucie",1,1,"N","AGGAAADAAGA")
    c.aventuriers.append(a1)
    c.aventuriers.append(a2)
    c.tour_de_jeu=tour(c.aventuriers)
    move=check_if_can_move(c,a2,new_index_y=2,new_index_x=2)
    assert move == 2

def test_aventurier_move_on_plain():
    c=carte(4,4)
    m1=mountain(1,0)
    m2=mountain(3,3)
    c.mountains.append(m1)
    c.mountains.append(m2)
    c.board[m1.axis_v][m1.axis_h]=display_mountain()
    c.board[m2.axis_v][m2.axis_h]=display_mountain()
    t=tresor(2,2,1)
    c.tresors.append(t)
    c.board[t.axis_v][t.axis_h]=t.display_tresor()
    a1=aventurier("john",3,2,"S","ADAGGADA")
    a2=aventurier("lucie",1,1,"N","AGGAAADAAGA")
    c.aventuriers.append(a1)
    c.aventuriers.append(a2)
    c.tour_de_jeu=tour(c.aventuriers)
    move=check_if_can_move(c,a2,new_index_y=1,new_index_x=2)
    assert move == 1

def test_aventurier_move_blocked_by_another_aventurier():
    c=carte(4,4)
    m1=mountain(1,0)
    m2=mountain(3,3)
    c.mountains.append(m1)
    c.mountains.append(m2)
    c.board[m1.axis_v][m1.axis_h]=display_mountain()
    c.board[m2.axis_v][m2.axis_h]=display_mountain()
    t=tresor(2,2,1)
    c.tresors.append(t)
    c.board[t.axis_v][t.axis_h]=t.display_tresor()
    a1=aventurier("john",3,2,"S","ADAGGADA")
    a2=aventurier("lucie",1,1,"N","AGGAAADAAGA")
    c.aventuriers.append(a1)
    c.aventuriers.append(a2)
    c.board[a1.axis_v][a1.axis_h]=a1.display_aventurier()
    c.board[a2.axis_v][a2.axis_h]=a2.display_aventurier()
    c.tour_de_jeu=tour(c.aventuriers)
    move=check_if_can_move(c,a1,new_index_y=2,new_index_x=3)
    assert move is None

def test_aventurier_move_blocked_by_mountain():
    c=carte(4,4)
    m1=mountain(1,0)
    m2=mountain(3,3)
    c.mountains.append(m1)
    c.mountains.append(m2)
    c.board[m1.axis_v][m1.axis_h]=display_mountain()
    c.board[m2.axis_v][m2.axis_h]=display_mountain()
    t=tresor(2,2,1)
    a1=aventurier("john",3,2,"S","ADAGGADA")
    a2=aventurier("lucie",1,1,"N","AGGAAADAAGA")
    c.aventuriers.append(a1)
    c.aventuriers.append(a2)
    c.tour_de_jeu=tour(c.aventuriers)
    move=check_if_can_move(c,a2,new_index_y=0,new_index_x=1)
    assert move is None
