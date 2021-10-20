# "PRIVATE" properties, functions:

# In python, all properties and functions are PUBLIC.
# They can be marked by the programmer (using underscore) to be MEANT TO BE private
# but they still are public!!!


class Pet:
    def __init__(self, name):
        self.name = name
        self._secret = "SECRET"


mouse = Pet("Mickey")
print(mouse.name)  # Mickey
print(mouse._secret)  # SECRET


# Note how PyCharm warns you about using the protected property "_secret"
# but allows you to do it anyway

# The recommendation is:
# Respect the pythonic convention of behaving as if properties and functions
# marked with "_" were truly private!


# CONTROLLING WHAT VALUES CAN BE SET TO PROPERTIES

class Teenager:
    def __init__(self, name, age) -> None:
        self._age = None
        self.name = name
        self.age = age

    @property
    def age(self) -> int:
        # Whenever in the code we try to access this property (like teenager_instance.age)
        # then this function is called and instead of the value in self.age, the value of
        # self._age is returned
        return self._age

    @age.setter
    def age(self, age_value: int) -> None:
        # This function is called also from the constructor
        if age_value < 13 or age_value > 19:
            raise ValueError(f"Age {age_value} is not a valid teenager age!")
        self._age = age_value

    # NOTE: Nothing prevents from setting "_age" directly!!!
    # So, we can set an illegal value to age.


matti = Teenager("Matti", 15)
print("Teenager created!")
print(f"Teenager {matti.name} is {matti.age} years old.")
# Teenager Matti is 15 years old.

# However, it is possible to directly set the "_age" to an illegal value!
# PyCharm does not wan you here!
matti._age = 10
print(f"Teenager {matti.name} is {matti.age} years old.")
# Teenager Matti is 10 years old.

# Next line will cause error!
lilli = Teenager("Lilli", 10)
# ValueError: Age 10 is not a valid teenager age!
