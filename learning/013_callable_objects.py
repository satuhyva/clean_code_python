# When a class has a "__call__" method implemented, we can use the class as a function
# in a way that has been defined in the "__call__" method.


class Basket:
    def __init__(self):
        self.ingredients = {}

    def __call__(self, ingredient, amount):
        if ingredient not in self.ingredients:
            self.ingredients[ingredient] = 0
        self.ingredients[ingredient] += amount
        return self.ingredients[ingredient]


# First an object is created:
basket = Basket()
# Then we use the object as a function
print(basket("pear", 3))
print(basket("pear", 1))
print(basket("pear", 2))


