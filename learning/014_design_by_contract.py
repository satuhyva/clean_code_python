# DESIGN BY CONTRACT (a design principle)
# When code cannot continue, an error will be raised.
# Designing a component that is used by a client.
# Making a contract on pre- and postconditions helps to spot where a fix should be made when an error occurs.

# Preconditions:
#       All the checking the code will perform before actually running.
#       These bind the client to supply proper input (that is in the contract).
#       Who should check that precondition requirements are met?
#       Usually in industry we use the demanding approach: the component validates the input it receives.
#       Which ever we choose, only one party should do the validation!

# Postconditions:
#       Checking done after the code has run.
#       These bind the component that it returns proper data to the client (that is in the contract)


# Invariants and side effects: Probably good to document with docstrings.


# Checking preconditions, performing the code and checking postconditions should be done by
# separate functions.



