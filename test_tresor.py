from tresor import tresor


def test_update_tresor():
    t1=tresor(1,2,3)
    t2=tresor(0,0,1)
    t1.update_tresor()
    t2.update_tresor()
    assert t1.nb_tresor==2
    assert t2.nb_tresor==0
