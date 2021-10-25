# MAP


# First let's see how the list-function works.
# The list function takes an iterable and turns it into a list.
items = ["apple", "cherry", "mango"]        # list
print(items)
# ['apple', 'cherry', 'mango']
print(list(items))
# ['apple', 'cherry', 'mango']
items = ("apple", "cherry", "mango")        # tuple
print(items)
# ('apple', 'cherry', 'mango')
print(list(items))
# ['apple', 'cherry', 'mango']
item = "cherry"                             # word
print(item)
# cherry
print(list(item))
# ['c', 'h', 'e', 'r', 'r', 'y']


# BASIC CASE:
# First you define the function with which each item in the map is calculated/created:
def multiply_by_two(number: int):
    return number + number


# Then you define the iterable from which the map will be created:
original_numbers = [1, 2, 3]
# Then you create the map:
doubled_numbers = map(multiply_by_two, original_numbers)
print(list(doubled_numbers))

# WITH LAMBDA:
# You can also use lambda expressions:
tripled_numbers = map(lambda x: x + x + x, original_numbers)
print(list(tripled_numbers))


# Combining to lists:
numbers_A = [1, 2, 3]
numbers_B = [4, 5, 6]
combined_numbers = map(lambda x, y: x + y, numbers_A, numbers_B)
print(list(combined_numbers))
# [5, 7, 9]


# NOTE: only those numbers is the lists that have a pair are included:
numbers_A = [1, 2, 3]
numbers_B = [4, 5]
combined_numbers = map(lambda x, y: x + y, numbers_A, numbers_B)
print(list(combined_numbers))
# [5, 7]



# WITH STRINGS:
names_list = ["Mark", "Boris"]
# Below each name is given to function "list" one at a time and converted to a list of letters
# which are then placed in the map
names_map = map(list, names_list)
print(list(names_map))
# [['M', 'a', 'r', 'k'], ['B', 'o', 'r', 'i', 's']]





