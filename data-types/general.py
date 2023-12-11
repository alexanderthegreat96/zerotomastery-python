import numpy as np
from collections import (
    deque, 
    Counter, 
    namedtuple
)
# data types in python

# a data type is a value in python
# every value holds a specific type
# or is of a specific type

# Fundamental data types

int # holds integers
float # holds floats / floating pooint numbers / numbers with decimal points
complex # holds a complex number This is equivalent to (real + imag*1j) where imag defaults to 0.
bin # not an actual data type, but rather a method that converts a number in binary
bool # holds either True or FalWse
str # any string
list # lists / arrays / ordered collections
tuple # immutable lists
set  # unordered collection of unique elements
dict # dictionary / map / associative array


# standard library provides built-in function for handling these types
# these methods will perform type conversion if necesarry
# the same types are useful for when type hinding something

my_int = int(22)
print(my_int)

my_float = float(22.1) 
print(my_float)

my_bool = True # False
print(my_bool)

my_str = str("this is my name")
print(my_str)

my_list = list() # can be initialied with [] as well
my_list.append(1)
my_list.append("string item")
print(my_list)

my_second_list = [12, 33, "hello"]
my_tuple = tuple(my_second_list) # tuples are immutable lists, that method takes a list as param and returns a tup[le]
print(my_tuple)

my_dict = dict() # one way of initializing this
my_dict["test"] = "some random value"
print(my_dict)

my_second_dict = {}
my_second_dict["hello"] = "world"
print(my_second_dict)

my_set = {23, 33, 11, 22, 31} # if a duplicate element is found, it is removed by default
print(my_set)

# Classes ->  custom types
class MyCar:
    def __init__(self, make: str, model: str):
        
        self._make = make
        self._model = model
        
    def honk(self):
        return self._make + " " + self._model + " is honking right now!"
    
car = MyCar(make="Audi", model="RS6")
print(car.honk())

# Specialized data types

# None
None
# signals nothing
my_empty_thing = None
print(my_empty_thing)
# Numpy Arrays
my_np_array = np.array([1, 232, 11, 334, 11])
print(my_np_array)


# queue and stacks
# The collections module provides specialized data types like deque for 
# double-ended queues and Counter for counting occurrences of elements.
my_queue = deque([1, 2, 3])
my_counter = Counter([1, 1, 2, 3, 3, 3])
print(my_queue)
print(my_counter)

# named tuples
# The collections module also provides namedtuple, 
# which is a lightweight alternative to defining classes when you need a simple object with named fields.
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p)

# These specialized data types provide additional functionality and features tailored to specific programming scenarios. 
# Depending on your needs, you can choose the appropriate data type to make your code more efficient and expressive.

# checking a specific type of a string

print(type(my_int)) # will return <class 'int'> -> yes, almost everthing in python is an objecs