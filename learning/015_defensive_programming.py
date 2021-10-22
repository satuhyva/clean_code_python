# DEFENSIVE PROGRAMMING (design principle)
# All parts of the program are able to protect themselves against invalid input.
# Mostly about how to handle errors (that we normally expect to occur)
# and how to handle errors that should never occur (assertions).


# ERROR HANDLING
# Errors we anticipate.
# How to gracefully handle them so that the program could continue.

# 1. Value substitution:
#       We need to decide, if an erroneous value can be substituted for something else.
#       For example, if a value to be added is not a number,
#       can we add 0 to total sum which will not change the total sum?
#       Sometimes we can use a default value (like opening browser at some localhost default port).

# 2. Exception handling:
#       Sometimes it is better to stop the program.
#       For example when contacting a database and it this fails.
#       As little exceptions as possible, because the client needs to prepare for them.
#       Exceptions should be handled at the correct level where they occur.
#       Do not propagate tracebacks to users (all details of what went wrong and where).
#       Return general messages like "Something went wrong".
#       Do not use empty exception blocks with only "pass".


# USING ASSERTIONS
# For situations that should never happen.


try:
    number = 7
    comparison_result = number < 5
    assert comparison_result, f"ERROR: {number} is not smaller than 5"
except AssertionError as error:
    print(error)
    # Do something because of this never-error!
    # For example log to some system this error and fail gracefully.
    # But make sure that the PROGRAM TERMINATES to this exception.


