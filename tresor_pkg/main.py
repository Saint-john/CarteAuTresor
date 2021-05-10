import os.path

from business.read_input import init_input
from business.tour import start_simulation
from business.write_result import write_output



def main():


    #lecture du fichier d'entrée et initialisation de tous les objets
    dirname_input="/resources/input"
    c=init_input(dirname_input)
    if c:
        # enclenchement de la simulation
        start_simulation(c)

        # écrire le résultat dans un fichier de sortie
        output_dirname="/resources/output"
        output_filename="/resources/resultat"
        write_output(c,output_dirname,output_filename)

if __name__ == "__main__":
    main()
