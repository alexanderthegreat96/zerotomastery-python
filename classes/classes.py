# Classes are what define object oriented programming
# Classes are objects
# Objects contain methods (aka functions)
# Why ?
# To create a layer of abstraction and organize code

# classes.py
class PlayerCharacter:
    
    # class object attribute
    # are used for static data
    # it will never change
    # besides from this, each method
    # has access to it

    membership = True

    # class constructor
    # it's what allows sharing of
    # variables between class methods / functions
    def __init__(self, name : str = "Annonymous", age : int = 0) -> None:
        
        self.name = "Annonymous"
        self.age = age

        if self.age > 18:
            self.name = name
            self.age = age
    

    # In Python, the @classmethod decorator is used to define a class method. 
    # A class method is a method that is bound to the class and not the instance of the class. 
    # It takes the class itself as its first parameter, conventionally named cls, instead of the instance.
    # takes cls instead of self
    
    @classmethod
    def adding_things(cls, num1 : int, num2 : int) -> int:
        return num1 + num2

    # returning a new class instance with the paramters
    @classmethod
    def build_class(cls, name : str, age : int) -> 'PlayerCharacter':
        return cls(name=name, age=age)

    
    # static methods are normal functions within classes
    # they can be called outside of the class
    # they do not depend on it's initialization similar to classmethods
    # but, have no access to the class' internals

    @staticmethod
    def modify_this(x : int) -> int:
        return x + 1

    def shout(self) -> None:
        print(f'My name is {self.name}')
        return