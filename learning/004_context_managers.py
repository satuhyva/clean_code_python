# When you need to run some code after something else
# For example when you need to close a file after reading it
# or close database connection after interacting with the database


# instead of this:
file = open("001_docstrings.py")
try:
    print("Do something with the file")
finally:
    file.close()

# do this (a more elegant, pythonic way):
with open("001_docstrings.py") as some_file:
    # now we are in context manager context
    print("Do something with the file")


# The "with" enters the context manager (__enter__), and "open" starts a protocol, which causes
# the opened file to be closed afterwards even if an exception occurred during handling it
# so cleaning up is always performed properly (__exit__)


# Context managers can be created by ourselves as well
# First the actions we want to be performed once we enter and exit the context:
def stop_working():
    print("STOPPED")


def start_working():
    print("START")


# Here we create our own context where we give the __enter__ and __exit__ functionalities
class WorkingContext:
    def __enter__(self):
        stop_working()
        return self

    # all the exc_s are related to a possible exception raised during running code while in context
    def __exit__(self, exc_type, exc_val, exc_tb):
        start_working()


def take_a_break_from_work():
    print("Having some coffee!!!")


with WorkingContext():
    take_a_break_from_work()

# A more compact way of doing it is with contextlib:
import contextlib


# Below is a generator function that will generate a Context Manager because it is
# assigned with the decorator "@contextlib.contextmanager"
@contextlib.contextmanager
def working_context_compact():
    try:
        stop_working()
        # this "yield" here makes this function a generator
        # everything before this "yield" becomes the "__enter__"-function
        yield
        # everything after this "yield" becomes the "__exit__"-function
    finally:
        start_working()


with working_context_compact():
    take_a_break_from_work()


# Yet another way of doing it with "contextlib.ContextDecorator" class extension:
class working_context_another_compact(contextlib.ContextDecorator):
    def __enter__(self):
        stop_working()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        start_working()


@working_context_another_compact()
def take_a_tea_break():
    print("Now drinking tea :)")


take_a_tea_break()



