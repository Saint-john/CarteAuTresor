import os
import pytest
from read_input import init_input
from read_input import verify_input_path
from read_input import get_files_in_dir
def test_init_input():
    """test la lecture de fichier"""
    c=init_input
    assert c

def test_verify_input_path():
    cwd,inputdir,dir=verify_input_path("/test_input_dir")
    #dir is boolean that means the directory exists
    assert dir
