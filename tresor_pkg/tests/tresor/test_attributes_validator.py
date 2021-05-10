from business import attributes_validator as v


def test_is_valid_number():
    assert v.is_valid_number(2)==2
    
def test_is_valid_width():
    assert v.is_valid_width(2)==2

def test_is_valid_width():
    assert v.is_valid_length(4)==4

def test_is_valid_string():
    assert v.is_valid_string("John")=="John"

def test_is_valid_orientation():
    assert v.is_valid_orientation("O") in "NSOE"
