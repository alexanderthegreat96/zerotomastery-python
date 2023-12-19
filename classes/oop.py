# the 4 pillars of OOP

# Encalulation
# = binding of functions and data
# we do this in one object aka class
# this data is essentially methods and attributes

class Myself:
    # class attributes
    my_attribute = "Hello"
    def __init__(self, me : str) -> None:
        self.class_attr = self.my_attribute
        self.me = me

    # methods
    def hello(self) -> None:
        print(self.me)
        print(self.class_attr)
        return

# Abstraction
# means: hiding information or abstracting info
# and only giving access to what's necessary

class Myself:
    # class attributes
    my_attribute = "Hello"
    def __init__(self, me : str) -> None:
        # these attributes are accessible from outside the class
        self.class_attr = self.my_attribute
        self.me = me

        # we only give access to what we think it's necessary
        # attributes accesible only by another class if it extends this one
        self._my_protected_attr = "Joe"

        # attributes only accessible from within this class
        self.__my_private_attr = "Mike"

    

    # methods
    def hello(self) -> None:
        print(self.me)
        print(self.class_attr)
        return
