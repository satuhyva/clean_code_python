# Annotations are a way of INFORMING others about data types.

from dataclasses import dataclass


# EXAMPLE 1:

# Here we gve suggestions of what data type the class properties should be
# (but these types are ONLY informative)
@dataclass
class Point:
    latitude: float
    longitude: float


def print_location_right(latitude: float, longitude: float) -> Point:
    print(f"{latitude}, {longitude}")
    return Point(1.3, 2.4)


print_location_right(2.3, 4.5)


# Note here how PyCharm warns you about wrong data types
# yet allows you to use them!!!
def print_location_wrong(latitude: float, longitude: float) -> Point:
    print(f"{latitude}, {longitude}")
    not_a_proper_point = Point('no', 22222)
    print(not_a_proper_point)
    return None


print_location_wrong(22, 'longitude')


# EXAMPLE 2:

# Another way to annotate function input type is to provide the type just above the function
# Also this in ONLY informative
Seconds = float


def start_working(delay_in_seconds: Seconds):
    pass


# And PyCharm only warns you about wrong data type, but allows you to use it.
start_working(5)
start_working('five')


# EXAMPLE 3:
Student = tuple[int, str]


def process_students(students: list[Student]):
    for student in students:
        print(student)


process_students([(1, "Onni"), (2, "Anni")])



