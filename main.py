from read_input import init_input
from tour import start_simulation
from write_result import write_output
def main():
    #lecture du fichier d'entrée et initialisation de tous les objets
    dirname_input="/input"
    c=init_input(dirname_input)
    if c:
        # enclenchement de la simulation
        start_simulation(c)

        # écrire le résultat dans un fichier de sortie
        output_dirname="/output"
        output_filename="/resultat"
        write_output(c,output_dirname,output_filename)

if __name__ == "__main__":
    main()
