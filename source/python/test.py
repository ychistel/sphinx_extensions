def occurrence(valeur,tab:list)->int:
    compteur = 0
    for elt in tab:
        if valeur == elt:
            compteur += 1
    return compteur

def nombre_valeurs(tab:list)->int:
    return len(tab)

t = [1,3,5,3,4,3]
assert occurrence(3,t) == 3, "Le nombre d'occurence est incorrect !"
assert nombre_valeurs(t) == 6, "Le nombre de valeurs est faux !"
print(occurrence(3,t))
print(nombre_valeurs(t))