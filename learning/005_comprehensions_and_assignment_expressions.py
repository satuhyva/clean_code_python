# FOR-loop, COMPREHENSION or ASSIGNMENT EXPRESSION?

# With a FOR-loop:
numbers = []
for i in range(5):
    numbers.append(f"{i}^2={i ** 2}")
print(numbers)

# With COMPREHENSION (create an array):
numbers = [f"{i}^2={i ** 2}" for i in range(5)]
print(numbers)
# ['0^2=0', '1^2=1', '2^2=4', '3^2=9', '4^2=16']


# Create a dictionary using comprehension:
numbers_dictionary = {str(i): i for i in [1, 2, 3]}
print(numbers_dictionary)
# {'1': 1, '2': 2, '3': 3}

fruits_array = ["apple", "orange", "banana"]
fruits_dictionary = {fruit: len(fruit) for fruit in fruits_array}
print(fruits_dictionary)
# {'apple': 5, 'orange': 6, 'banana': 6}

fruits_capitalized_dictionary = {fruit: fruit.capitalize() for fruit in fruits_array}
print(fruits_capitalized_dictionary)
# {'apple': 'Apple', 'orange': 'Orange', 'banana': 'Banana'}


# Reversing keys and values in a dictionary:
# NOTE: the ".items()" is needed below to make the dictionary into a list
fruits_dictionary_reversed = {value: key for key, value in fruits_dictionary.items()}
print(fruits_dictionary_reversed)
# {5: 'apple', 6: 'banana'}
# NOTE: 'orange' is now missing because it has the same key (5) ans apple!!!


# Removing some items in the dictionary using comprehension:
berries = ["strawberry", "bilberry", "blackcurrant", "lingonberry", "raspberry"]
berries_all = {berry: len(berry) for berry in berries}
print(berries_all)
# {'strawberry': 10, 'bilberry': 8, 'blackcurrant': 12, 'lingonberry': 11}

berries_to_remove = {"lingonberry", "blackcurrant"}
berries_some = {berry: berries_all[berry] for berry in berries_all.keys() - berries_to_remove}
print(berries_some)
# {'bilberry': 8, 'raspberry': 9, 'strawberry': 10}

# In python you can do this:
print({"strawberry", "bilberry", "blackcurrant"} - {"bilberry"})
# {'strawberry', 'blackcurrant'}

