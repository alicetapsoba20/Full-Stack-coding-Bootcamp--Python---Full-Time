#Exercice 5 : Mot Le Plus Long Sans Caractère Spécifique

#phrase = input("veuiller saisir la phrase la plus longue possible sans le caractère "A" : ")
phrase2=""
phrase1 = input ("saisir la phrase la plus longue possible sans le caractère A: ")
while True :

    phrase = input ("veuiller saisir la phrase la plus longue possible sans le caractère A: ")
    phrase1 = str(phrase)
    if "A" in phrase1 :
        print("error")
    else:
        long_phrase1 = len(phrase1)
        long_phrase2 = len (phrase2) 
        
    if long_phrase1>long_phrase2  :
        print("félicitations vrotre phrase est la plus longue")
        phrase2=phrase1
        phrase = input ("saisir la phrase la plus longue possible sans le caractère A: ")