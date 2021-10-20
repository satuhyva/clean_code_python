
# Enumerate takes an iterable and returns the element and its index
for index, value in enumerate(['A', 'B', 'C']):
    print(f"{index}: {value}")
# 0: A
# 1: B
# 2: C

fruits_array = ["apple", "orange", "banana"]
fruits_index_dictionary = {fruit: index for index, fruit in enumerate(fruits_array)}
print(fruits_index_dictionary)
# {'apple': 0, 'orange': 1, 'banana': 2}

