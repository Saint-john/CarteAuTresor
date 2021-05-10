from model.carte import carte
from model.mountain import mountain
from model.tresor import tresor
from model.aventurier import aventurier


def test_carte():
        c=carte(10,3)
        assert c

def test_mountains_position_is_inside_the_board():
    c=carte(4,3)
    c.mountains.append(mountain(3,1))
    c.mountains.append(mountain(2,2))
    c.mountains.append(mountain(3,2))
    for i in c.mountains:
        assert 0 < i.axis_h < c.largeur
        assert 0 < i.axis_v < c.longueur

def test_tresors_is_inside_the_board():
    c=carte(4,5)
    c.tresors.append(tresor(2,2,3))
    c.tresors.append(tresor(1,2,2))
    c.tresors.append(tresor(3,3,1))
    for i in c.tresors:
        assert 0 < i.axis_h < c.largeur
        assert 0 < i.axis_v < c.longueur

def test_aventurier_position_is_inside_the_board():
    c=carte(4,4)
    c.aventuriers.append(aventurier("john",3,2,"S","ADAGGADA"))
    c.aventuriers.append(aventurier("linda",1,2,"N","ADDDAGAGGA"))
    c.aventuriers.append(aventurier("luc",3,3,"O","AAADDAAGADDAAAAA"))
    for i in c.aventuriers:
        assert 0 < i.axis_h < c.largeur
        assert 0 < i.axis_v < c.longueur
        assert type(i.name) == str
        assert i.orientation in ("S","N","O","E")
        assert type(i.chemin) == str
