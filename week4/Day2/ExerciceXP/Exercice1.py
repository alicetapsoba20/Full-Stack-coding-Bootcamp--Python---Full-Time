#Exercice 1 : Set

my_fav_numbers = set ()
my_fav_numbers = {3,6,12,14,24,30 }
my_fav_numbers.add(4)
my_fav_numbers.add(10)
my_fav_numbers.pop()
print(my_fav_numbers)
friend_fav_numbers = set()
friend_fav_numbers ={11,5,27,14,12}
our_fav_numbers = set()
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)