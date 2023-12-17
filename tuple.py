"""
    U Pithon-u, tuple je tip podataka kolekcije koji je sličan listi, ali je nepromenljiv. 
    To znači da kada se jednom kreira tuple, ne možete menjati njegove elemente. 
    Korke se definišu zatvaranjem niza vrednosti odvojenih zarezima u zagradama. Evo osnovnog primera:
"""

# Creating a tuple
my_tuple = (1, 2, 3, 'a', 'b', 'c')

# Accessing elements in a tuple
print(my_tuple[0])  # Output: 1
print(my_tuple[3])  # Output: 'a'

# Slicing a tuple
print(my_tuple[1:4])  # Output: (2, 3, 'a')

# Tuple concatenation
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)  # Output: (1, 2, 3, 'a', 'b', 'c')


#koristi se za hes mape, ne mozemo koristii liste zato sto one nisu hesabilne