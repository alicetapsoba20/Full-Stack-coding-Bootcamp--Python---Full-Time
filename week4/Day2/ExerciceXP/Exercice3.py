#Exercice 3 : Liste

from itertools import count


basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0,"Apples")
k = basket.count ("Apples")
print(basket)
print(k)
basket.clear()
print(basket)
