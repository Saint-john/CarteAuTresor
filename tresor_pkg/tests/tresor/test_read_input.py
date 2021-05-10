from business.read_input import init_input
from business.read_input import verify_input_path


def test_init_input():
    """test la lecture de fichier"""
    c=init_input
    assert c

def test_verify_input_path():
    cwd,inputdir,dir=verify_input_path("/input")
    #dir is boolean that means the directory exists
    assert dir
