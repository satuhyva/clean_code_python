# Lists, tuples sets and dictionaries are "built-in" iterables
# that can be iterated over a for loop.
# You can also build your own iterables.

# FIRST implementation:
# NOTE: This iterable works only once:

class OnceOnlyNumberIterable:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.current = first

    # This method returns self, telling that the object made from this class
    # is itself the iterable (for which the "__next__" needs to be called)
    def __iter__(self):
        return self

    # And because the object itself is an iterable, this "__next__" method is called when iterating
    # Here it is described how the next element is created and it is returned.
    def __next__(self):
        if self.current > self.last:
            # "StopIteration" is needed to stop iteration.
            raise StopIteration()
        # first memorize the current number so that we can return also the very first one
        number_now = self.current
        self.current += 1
        return number_now



number_iterable = OnceOnlyNumberIterable(3, 8)
for number in number_iterable:
    print(number)
# If we try to iterate again THE SAME object "number_iterable" that has just been iterated over,
# it won't work anymore. Nothing is printed from the loop below:
for number in number_iterable:
    print(number)


# SECOND implementation:
# Either always create a new iterator OR:

class ContinuouslyFunctioningNumberIterable:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    # Here we instead have "while" loop and "yield"
    def __iter__(self):
        current = self.first
        while current < self.last:
            yield current
            current += 1


# Now iteration can be performed several times as the "__iter__" always returns
# the same iterable
number_iterable = ContinuouslyFunctioningNumberIterable(3, 6)
for number in number_iterable:
    print(number)
for number in number_iterable:
    print(number)


# Difference:
# For-loop always calls the "__iter__" function.
# In the first class, the self.current changes and after the first iteration
# the condition self.last has been reached.
# In the second class we always return a new iterator that starts from the first.
# The problem with this approach is that if you want the last element,
# you need to iterate till the end!
# If a sequence is implemented, each element can be reached quickly,
# but more memory is needed. See next.

# THIRD implementation:
class SequenceNumberIterable:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self._range = self._create_range()


    def _create_range(self):
        numbers = []
        current = self.first
        while current <= self.last:
            numbers.append(current)
            current += 1
        return numbers

    def __getitem__(self, index):
        return self._range[index]

    def __len__(self):
        return len(self._range)


number_iterable = SequenceNumberIterable(0, 4)
for number in number_iterable:
    print(number)
print(number_iterable[2])




