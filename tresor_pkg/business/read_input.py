import os
from model.carte import carte
from model.Display import display_mountain, display_plain
from model.mountain import mountain
from model.tresor import tresor
from model.aventurier import aventurier
from business.tour import tour


def init_input(dirname_input):
    carte_created = False

    cwd, inputdir, dir = verify_input_path(dirname_input)

    if not dir:
        os.makedirs(inputdir, exist_ok=True)
        print(f"Le dossier d'entrée vient d'être créé, veuillez ajouter votre fichier d'entrée ici. {inputdir}")
    else:
        getfile = get_files_in_dir(inputdir)
        if getfile:

            if len(getfile) > 1:
                print(
                    f"Plusieurs fichiers d'entrée sont dans le directory{inputdir}:\n{getfile}, seul le premier est pris en compte.")
            #    selectedfile=raw_input(f"Plusieurs fichiers d'entrée sont présents dans {inputdir} lequel voulez vous utilisez ? \n {getfile}:")
            #    print(selectedfile)
            input = open(inputdir + "/" + getfile[0], "r")

            for l in input:
                if l[0] == "C" and carte_created:
                    print(
                        "une carte a déjà été instancié, cette ligne ne sera pas prise en compte seul une carte peut-etre créé à la fois.")
                elif l[0] == "C" and not carte_created:
                    str = l.replace(" ", "")
                    values = str.split("-")
                    try:
                        largeur = int(values[1])
                        longueur = int(values[2])
                    except ValueError:
                        print(" Les valeurs attendues sont des entiers. veuillez modifier le fichier.")
                    c = carte(largeur, longueur)
                    carte_created = True
                    print(f"La carte a ete cree. [{largeur} unites en largeur, {longueur} unites en longueur]")

                if l[0] == "M":
                    str = l.replace(" ", "")
                    values = str.split("-")
                    try:
                        axis_h = int(values[1])
                        axis_v = int(values[2][0])
                    except ValueError:
                        print(" Les valeurs attendues sont des entiers. veuillez modifier le fichier.")

                    if not 0 <= axis_h < c.largeur or not 0 <= axis_v < c.longueur:
                        print("La case n'est pas dans la carte, la ligne est ignoré.")
                    else:
                        if c.board[axis_h][axis_v] in display_plain():
                            c.mountains.append(mountain(axis_h, axis_v))
                            print(f"On aperçoit une montagne en [{axis_h},{axis_v}]")
                            c.board[axis_h][axis_v] = display_mountain()
                        else:
                            print(
                                "Cette case n'est pas une plaine, cette montagne ne peut etre créé ici. La ligne est donc ignoré")

                if l[0] == "T":
                    str = l.replace(" ", "")
                    values = str.split("-")
                    try:
                        axis_h = int(values[1])
                        axis_v = int(values[2])
                        nb_tresors = int(values[3][0])
                    except ValueError:
                        print(" Les valeurs attendues sont des entiers. veuillez modifier le fichier.")

                    if not nb_tresors > 0:
                        print("le nombre de tresor doit être un entier positif non nul.")
                    else:
                        if not 0 <= axis_h < c.largeur or not 0 <= axis_v < c.longueur:
                            print("La case n'est pas dans la carte, la ligne est ignoré.")
                        else:
                            if c.board[axis_v][axis_h] in display_plain():
                                c.tresors.append(tresor(axis_h, axis_v, nb_tresors))
                                print(f"{nb_tresors} trésors ont été caché ici. [{axis_h},{axis_v}]")

                            else:
                                print(
                                    "Cette case n'est pas une plaine, le trésor ne peut pas être créé ici. La ligne est donc ignoré.")

                if l[0] == "A":
                    str = l.replace(" ", "")
                    values = str.split("-")

                    try:
                        name = values[1]
                        orientation = values[4]
                        parcours = values[5]
                        axis_h = int(values[2])
                        axis_v = int(values[3])
                        nb_tresors = int(values[6])
                    except ValueError:
                        print(" Les valeurs attendues sont des entiers. veuillez modifier le fichier.")

                    if not 0 <= axis_h < c.largeur or not 0 <= axis_v < c.longueur:
                        print("La case n'est pas dans la carte, la ligne est ignoré.")
                    else:
                        if not orientation in "NSOE":
                            print(
                                "L'orientation renseigné n'est pas reconnu, toute triche est sanctionné, la ligne est ignoré.")
                        else:
                            c.aventuriers.append(aventurier(name, axis_h, axis_v, orientation, parcours, nb_tresors))
                            print(
                                f"l'aventurier {name} est inscrit. il partira de [{axis_h},{axis_v}] et s'orientera vers {orientation}")

            for t in c.tresors:
                c.board[t.axis_v][t.axis_h] = t.display_tresor()
            for a in c.aventuriers:
                c.board[a.axis_v][a.axis_h] = a.display_aventurier()
            c.design_map()
            input.close()

            c.tour_de_jeu = tour(c.aventuriers)
            return c
        else:
            print(
                "Pas de fichier d'entrée présent dans :" + inputdir + "\n\n\t Veuillez créer un fichier dans ce repertoire")
            return


def verify_input_path(dirname_input):
    print("La carte au trésor !")
    cwd = os.getcwd()
    inputdir = cwd + dirname_input
    dir = os.path.exists(inputdir)
    return cwd, inputdir, dir


# list of files
def get_files_in_dir(dir):
    return os.listdir(dir)
