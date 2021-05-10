import os
def write_output(c,dirname,filename):
    cwd=os.getcwd()
    outputdir=cwd+dirname
    os.makedirs(outputdir,exist_ok=True)
    outputfile=outputdir+filename
    output = open(outputfile, "w")
    print("Le fichier du résultat de la simulation a été créé:"+outputfile)
    design_result(c,output)
    output.close()

def design_result(c,file):
    write_line_carte(c,file)
    write_lines_mountains(c,file)
    write_lines_tresors(c,file)
    write_lines_aventuriers(c,file)
    write_board(c,file)
    write_tips(c,file)

def write_line_carte(c,file):
    file.write(f"#C comme carte - axe horizontal - axe vertical \n")
    file.write(f"C"+" - "+str(c.largeur)+" - "+str(c.longueur)+"\n")

def write_lines_mountains(c,file):
    file.write(f"#M comme montagne - axe horizontal - axe vertical \n")
    for i in c.mountains:

        file.write(f"M - "+str(i.axis_h)+" - "+str(i.axis_v)+"\n")

def write_lines_tresors(c,file):
    file.write(f"#T comme tresor - axe horizontal - axe vertical - nombre de tresors restant \n")
    for i in c.tresors:
        file.write(f"T - "+str(i.axis_h)+" - "+str(i.axis_v)+" - " + str(i.nb_tresor)+"\n")

def write_lines_aventuriers(c,file):
    file.write(f"#A comme aventurier - nom de l'aventurier - axe horizontal - axe vertical - orientation - nombre de tresors ramasses \n")
    for i in c.aventuriers:
        file.write(f"A - "+i.name+" - "+str(i.axis_h)+" - "+str(i.axis_v)+" - " + i.orientation +" - "+ str(i.tresors)+"\n")

def write_board(c,file):
    file.write("\n\n\t El mapa de la madre de dios \n\n")

    for i in c.board:
        file.write(" ".join(i)+"\n")
def write_tips(c,file):
    file.write("\n\n\n\n\t Consigne: Les numeros sur la carte represente le tour dans lequel l'aventurier occupait cette position. (par exemple si je ne bouge pas le tour 2 mais que le tour 3 je me deplace alors le (tour-1=2) apparaitra sur la position precedente \n\n")
