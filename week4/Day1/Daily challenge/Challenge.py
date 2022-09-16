                #Question 1:
from random import random


chaine = input ("Entrer une chaine de 10 caractère : ")
c = len(chaine)
if c < 10:
    print("chaine pas assez longue")
elif c > 10:
    print("chaine trop longue")
else:
    print (c)

            #Question 2:

print(chaine[0])
print(chaine[-1])

             #Question 3:
import random
a =" "
for i in chaine :
    a = a + i
    print(a)

             #Question 4:
ch = list(chaine)
random.shuffle(ch)
print("".join (ch))