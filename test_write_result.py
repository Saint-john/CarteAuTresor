from carte import carte
from write_result import write_output
def test_write_result_in_file():
    c=carte(5,5)
    write_output(c,"/output","/test_resultat")
