from exo_diapo1_1 import parse_tlds

parse_tlds();

def dico():
    words = ["tortue", "building", "manger", "ordinateur", "vacances", "portable", "mayo"]
    dico = {}
    for word in words:
        dico[word] = len(word)
    
    print(dico)