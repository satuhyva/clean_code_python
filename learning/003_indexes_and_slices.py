fruits = ['apple', 'kiwi', 'orange', 'banana', 'pear']


# first element is at 0 (and is apple)
print(fruits[0])


# in the "traditional way" the last element is
print(fruits[len(fruits) - 1])
# in the "PYTHONIC" WAY the last element is at -1 (and is pear)
print(fruits[-1])

# to get a "slice" of an array (kiwi, orange):
# (element at start index 1 is included but element at end index 3 is not included)
print(fruits[1:3])

tuple_data = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
print(tuple_data[:2])       # a, b
print(tuple_data[2:])       # c, d, e, f, g
print(tuple_data[1::2])     # b, d, f

