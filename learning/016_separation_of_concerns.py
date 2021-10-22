# SEPARATION OF CONCERNS   (both code and architecture)
# Each component should be responsible for only one thing and it should
# NOT know about the rest.

# With separation of concerns we try to prevent ripple effects
# (propagation of change in one component to distant other components).
# We want to maintain the change and we want the code to be easy to change.

# Cohesion =
#   - object should have a small, well-defined purpose
#   - object should do as little as possible

# Coupling =
#   - the situation when objects depend on other objects
#   - code reuse becomes more difficult, ripple effects




# DRY (DON'T REPEAT YOURSELF)
#   * "Things" must exist only in singular in only one place
#   * When we need to do a change, we do it only in one place. This is less error prone.
#   * We save by not wasting on redoing things.
#   * When you have some knowledge in the code, acknowledge it! See below:

points = {"matti": 23, "antti": 33}
# Here we call twice for the points by Matti, not acknowledging that the result is knowledge
print(points["matti"] > 30)
print(f"Matti's points: {points['matti']}")
# Here we acknowledge the knowledge of Antti's points and then use it
# without duplicating the call to dictionary:
points_by_antti = points["antti"]
print(points_by_antti > 30)
print(f"Antti's points: {points_by_antti}")



# YAGNI (YOU AIN'T GONNA NEED IT)
# Maintainable software is not about anticipating future requirements.
# Rather it is about writing code that addresses current requirements in a way
# that makes it possible and easy to later change the code to meet future requirements.



# KIS (KEEP IT SIMPLE)
# Find the solution that is the minimal one to the problem.
# Make the solution as simple as possible. The simpler it is, the more maintainable it is.



# EAFP (EASIER TO ASK FORGIVENESS THAN PERMISSION)
#       First write some code, then try if it works by running it, and handle errors.
#       For example, open a file and if the file does not exist, handle the exception.
# LBYL (LOOK BEFORE YOU LEAP)
#       First check, then act.
#       For example, before opening a file with some name first check whether the file exists,
#       and only then open the file.
# HERE IT IS RECOMMENDED: use EAFP!
















