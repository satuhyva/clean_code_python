# With the "__getattr__" method we can implement our own way of dealing with
# object attributes that do not exist but are called for.


class DynamicBox:
    def __init__(self, content):
        self.content = content

    def __getattr__(self, item_of_interest):
        if item_of_interest.startswith("coming_soon"):
            item = item_of_interest.replace('coming_soon_', '')
            return f"{item} is coming soon"
        raise AttributeError(f"{self.__class__.__name__} will not contain {item_of_interest} for any time soon")


# First create a box and place there an item to be the content.
# When we call for "content", Python will call the "__getattribute__" method to get the content:
box = DynamicBox("old jeans")
print(box.content)
# old jeans

# Next we are calling for an attribute that does not exist, so the "__getattribute__" method
# cannot find it. That is why the "__getattr__" method that we have implemented is called.
print(box.coming_soon_jacket)
# jacket is coming soon




# Next we can create the attribute permanently by adding to class parameter dictionary object
# the attribute "coming_soon_jacket". The dictionary already holds the attribute content.
# First let's print the class dictionary:
print(box.__dict__)
# {'content': 'old jeans'}
box.__dict__["coming_soon_jacket"] = "JACKET"
print(box.__dict__)
# {'content': 'old jeans', 'coming_soon_jacket': 'JACKET'}
# NOTE: now the return value is different. The "__getattribute__" function finds the attribute, so our own
# "__getattr__" implementation is not used:
print(box.coming_soon_jacket)
# JACKET



print(box.avocados)
# AttributeError: DynamicBox will not contain avocados for any time soon

