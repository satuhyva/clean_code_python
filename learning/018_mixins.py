# MIXINS:

# The next class creates an iterator, that contains the words of the phrase it is given in constructor
class Splitter:

    def __init__(self, phrase):
        self.phrase = phrase

    def __iter__(self):
        yield from self.phrase.split(" ")


for word in Splitter("Three little words"):
    print(word)
# Three
# little
# words

# Here Splitter is the BASE class.


# Before next, see from the next file (019_map.py) how a map works in python.
# Then we define a MIXIN class:
class UppercaseMixin:

    # Here "super().__iter__()" returns the iterable that contains the words as a list.
    # These words are give one by one to the "upper"-function and converted to uppercase.
    # And a map is created of these words in lists of uppercase letters and returned as an iterable.
    def __iter__(self):
        return map(str.upper, super().__iter__())
    # NOTE: Here PyCharm complains that "__iter()__" is unresolved.
    # This is probably because UppercaseMixin does not inherit any parent.
    # UppercaseMixin is a mixin that CANNOT be used on its own, it has to be used with another
    # class (that is NOT its parent), but which it "inherits" because of "resolution order", like below.


# Here no code is needed, only we need to mix the upper casing functionality with some iterator.
# Now we could use the upper casing functionality with some other iterator too!
class UppercaseSplitter(UppercaseMixin, Splitter):
    pass


# Now UppercaseMixin has a parent, Splitter, from which it can inherit the "__iter__"-function!
print([some_class.__name__ for some_class in UppercaseSplitter.mro()])
# ['UppercaseSplitter', 'UppercaseMixin', 'Splitter', 'object']

for word in UppercaseSplitter("Three little words"):
    print(word)