#Exercice 8 : Comment T'appelles-Tu ?

from unicodedata import name

name = input("Quel est votre nom : ")
name1 = "TAPSOBA"
nam = name1.lower()
if name == name1 or name== nam:
    print("YOUPiiiiii on a le meme nom. ")
elif name !=name1 or name== nam:
    print("ooohhhh désolé on a pas le meme nom.")


