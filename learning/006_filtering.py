# First let's create a filtering decision-making function:
# If the function returns "True", then the item being tested
# should be included in the resulting iterable
def should_be_included_test(letter):
    if letter.islower():
        return False
    return True


strings = ["AAAAHEA", "adffaa", "TEWEDW", "fcdsfs", "WEWLFJHNR", "sss"]
# Note: filter returns an ITERABLE
filtered_strings = filter(should_be_included_test, strings)
# to iterate over the filtered letters with a for loop:
for item in filtered_strings:
    print(item)
