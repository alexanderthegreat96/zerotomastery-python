# "Dunder" is short for "double underscore," and dunder methods in Python are special 
# methods that have double underscores at the beginning and end of their names. 
# These methods are also known as magic methods or special methods, and they provide 
# a way for classes to define certain behaviors that can be invoked implicitly.

# short story, they start with __ and and in __
# and are also known as magic methods


from typing import Any


class MyToy:
    # dunder method for defining the constructor of a class

    def __init__(self) -> None:
        pass
    
    # calls the str() function and returns a humandly readable text
    # in otheer words, it modifies the behaviour of str() 
    def __str__(self) -> str:
        pass

    # same goes for len
    def __len__(self):
        return len()
    
    # call method
    # The __call__ method is another special method in Python 
    # that allows an object to be called as if it were a function. 
    # By defining the __call__ method in a class, you can make 
    # instances of that class callable.
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass