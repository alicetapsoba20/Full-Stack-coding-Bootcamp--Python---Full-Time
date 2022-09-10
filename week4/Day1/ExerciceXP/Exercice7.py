from contextlib import nullcontext


num = input ("veuillez entrer un nombre : ")
numb = int (num)
if numb % 2 == 0 :
    print("ce nombre est paire.")
else:
    print("Ce nombre est impaire.")
