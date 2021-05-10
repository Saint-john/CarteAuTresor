def is_valid_number(attr):
    if type(attr) is not int:
        raise ValueError("Un nombre est attendu")
    else:
        if attr < 0:
            raise ValueError("la position minimal est 0")
    return attr

def is_valid_width(attr):
    if type(attr) is not int:
        raise ValueError("Un nombre est attendu")
    else:
        if attr < 1:
            raise ValueError("la largeur doit être superieur à 0")
    return attr

def is_valid_length(attr):
    if type(attr) is not int:
        raise ValueError("Un nombre est attendu")
    else:
        if attr < 1:
            raise ValueError("la longueur doit être superieur à 0")
    return attr

def is_valid_string(attr):
    if type(attr) is not str:
        raise ValueError("Une chaine de caractere est attendu")
    return attr

def is_valid_orientation(attr):
    if type(attr) is not str:
        raise ValueError("Une chaine de caractere est attendu")
    else:
        if len(attr) > 1:
            raise ValueError("un seul caractère est attendu pour l'orientation")
        else:
            if not attr in "NSOE":
                raise ValueError("l'orientation n'est pas reconnu parmis N S O ou E")
    return attr
