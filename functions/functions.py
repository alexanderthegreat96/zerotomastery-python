# the most basic way to implement re-usable code

# functions receive paramters
# parameters can implement type hinting

def my_detais(my_name : str = "Alex", 
              my_age : int = 27, 
              my_hobbies : list = ["guitar", "coding", "gaming", "women"]) -> None:
    
    print(f'Hello there, {my_name} !')
    print(f'You are {my_age}')
    
    print("You seem to like: ")
    for hobby in my_hobbies:
        print(" - " + hobby)

my_detais()

# arguments vs parameters
# arguments are actually the values used inside the function
# parameters are essentially giving arguments their value


# functions receive parameters
# when working with parameters 
# inside the function, we reffer to them
# as arguments

def my_func(argument1 : str, argument2: str):
    # this is what arguments look like
    print(argument1, argument2)

my_func("Hello", "There") # this is what parameters look like

# we also have variable arguments and variable keyword arguments
# when using **kwargs, the parameters must be key-value pairs
# ex: first_name = "John Done"

def print_names(**kwargs) -> None:
    '''
        Using **kwargs, which reffers to variable keyword arguments
        Ex: your_name = "Someone There"
    '''
    for key, value in kwargs.items():
        print(key, value)

print_names(first_name = "Alex", last_name = "John", middlename = "Mathew")

def sum_numbers(*args):
    total = 0
    for number in args:
        total += number
    return total

print(sum_numbers(12, 121, 12))

# methods vs functions
# a method is a function but within a class

class Student:

    def __init__(self, full_name : str) -> None:
        self.__full_name = full_name

    def say_hello(self):
        print("Hello, " + self.__full_name)

greet = Student("Andrei Neagoaie")
greet.say_hello()

# what is scope?
# Scope = what variables do I have access to

# global keyword

so_far = 0
def count_numbers():
    global so_far 
    so_far += 1

count_numbers() 
count_numbers()
count_numbers()
count_numbers()
count_numbers()

print(so_far)
