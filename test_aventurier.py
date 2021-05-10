from aventurier import aventurier
from carte import carte
def test_aventurier():
    a=aventurier("john",3,2,"N","ADAGGADA")
    assert a

def test_move_forward():
    c=carte(5,5)
    a=aventurier("john",3,2,"S","ADAGGADA")
    a.move_forward(c,4,2)
    assert a.axis_h==4
    assert a.axis_v==2
    assert c.board[a.axis_v][a.axis_h]==a.display_aventurier()

def test_pivot_left():
    a=aventurier("john",3,2,"S","ADAGGADA")
    a.pivot_left()
    assert a.orientation == "E"

def test_pivot_right():
    a=aventurier("john",3,2,"O","ADAGGADA")
    a.pivot_right()
    assert a.orientation == "N"

def test_get_tresor():
    a=aventurier("john",3,2,"O","ADAGGADA")
    a.get_tresor()
    assert a.tresors == 1
