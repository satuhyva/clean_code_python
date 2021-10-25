# INHERITANCE
# issue with inheritance: the inheriting class depends on the parent class
# (the child is tightly coupled with the parent) and coupling is one thing
# we want to avoid when writing reusable code...

# Rethink of inheriting, if you do not need most of the parent's functions in the child class
# or if you need to rewrite many of them. Is the parent doing too much? Is the child not a proper subclass?
# A good use case is that the child needs most of the functions of the parent and then needs some
# special functions of its own. Keyword for inheriting is SPECIALIZATION. The child specializes.
# A good example are Exceptions (parent) with their children (custom defined exceptions).

# Multiple inheritance:
# If not done correctly, multiplies problems.
# MRO (Method resolution order):
# Multiple inheritance is often feared: If the different inherited classes overwrite the same
# parent method, which method is it using???

class Base:
    module_name = "Base"

    def __init__(self, module_name):
        self.name = module_name

    def __str__(self):
        return f"{self.module_name}: {self.name}"


# Here class Intermediate1 inherits the "__init__" method, so the "module_name" that is
# given in the constructor will be set to "self.name" but the "module.name" gets a new value:
class Intermediate1(Base):
    module_name = "Intermediate 1"


class Intermediate2(Base):
    module_name = "Intermediate 2"


class ChildModule(Intermediate1, Intermediate2):
    pass


# We create instance of class ChildModule and the argument is "Child".
# Intermediate1 inherits the "__init__" method from Base and sets the "self.name"
# to the value of "module_name" which is "Child". The value of "module_name" in
# Base is originally "Base", but Intermediate1 resets this and it is set to
# Intermediate 1. So, when we call the "__str__"-method of the instance of
# ChildModule, the "self.module_name" is "Intermediate1" and the "self.name" is "Child".
print(ChildModule("Child"))


# Intermediate 1: Child


# If we change the order in inheritance to bethe other way around,
# the "self.module_name" is different:
class ChildModule2(Intermediate2, Intermediate1):
    pass


print(ChildModule2("Child"))
# Intermediate 2: Child
# To get the resolution order:
print([a_class.__name__ for a_class in ChildModule2.mro()])
# mro = Method Resolution Order

# ['ChildModule2', 'Intermediate2', 'Intermediate1', 'Base', 'object']
# Here we see that first "Module_name" has been set to "Base", then to "Intermediate 1"
# and then to "Intermediate 2" (and ChildModule2 does not set a new value to it).


# This "order of inheritance" or "resolution order" can be exploited with mixins.
# See the next file "018_mixins.py".




