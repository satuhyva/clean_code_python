# Container objects have a "__contains__" method that tells
# with a boolean value whether the container contains the element
# We need the "__contains__" to be implemented to be able to use:
# "if element in list"-type of code.

# First we create a class that has the "__contains__" function implemented
# returning information on whether some position is within the area.
# The purpose of "AreaBoundary" is to only tell if the position is in the area.
class AreaBoundary:
    def __init__(self, horizontal, vertical):
        self.horizontal = horizontal
        self.vertical = vertical

    def __contains__(self, position):
        horizontal_position, vertical_position = position
        return 0 <= horizontal_position <= self.horizontal and 0 <= vertical_position <= self.vertical


# Then we have the actual area object.
# It also has the "__contains__" method implemented.
# We could have written the above implementation directly here, but this way is more informative.
# It is now more clear for the reader that we want to check if "position in area"
# and the logic is hidden in AreaBoundary.
class Area:
    def __init__(self, horizontal, vertical):
        self.horizontal = horizontal
        self.vertical = vertical
        self.area_boundary = AreaBoundary(horizontal, vertical)

    def __contains__(self, position):
        return position in self.area_boundary


area = Area(3, 3)
some_position = 2, 3
if some_position in area:
    print("is")
else:
    print("is not")
another_position = 2, 4
if another_position in area:
    print("is")
else:
    print("is not")




