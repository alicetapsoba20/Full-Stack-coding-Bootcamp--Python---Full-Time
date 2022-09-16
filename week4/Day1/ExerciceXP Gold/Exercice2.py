#Exercice 2 : Quelle Est La Saison ?

mois = input("veuillez saisir un mois (1 à 12) : ")
mois1 = int(mois)
if mois1 >= 3 and mois1 <= 5:
    print("C'est le printemps")
elif mois1 >= 6 and mois1 <= 8:
    print("C'est l'été")
elif mois1 >= 9 and mois1 <= 11:
    print("C'est l'automne")
elif mois1 == 12 or mois1 == 1 or mois1 == 2:
    print("C'est l'hiver")
else :
    print("veuillez Saisir un mois s'il vous plait (1 à 12) : ")
