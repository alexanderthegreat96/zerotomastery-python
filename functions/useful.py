# .map(), .filter(), .zip(), .reduce()

# map function
# allows you to do something for every
# element of the list, like in javascript
# In Python, the map() function is a built-in function that applies a specified function to all items in an iterable 
# (e.g., a list) and returns an iterator that produces the results. The syntax for the map() function is as follows:

def square(x : int) -> int:
    return x ** 2;

numbers = [2, 4, 12, 22, 33]
squared_numbers = map(square, numbers)
print(list(squared_numbers))
print(list(map(lambda x: x **2, numbers))) # we gave it an inline function


# filter function
# applies the given function to all elements of the list
# the function supplied must return true or false
def check_if_odd(x : int) -> int:
    return x % 2 != 0 # will evalutate to True or False

odd_numbers = filter(check_if_odd, numbers)
print(list(odd_numbers))

# zip function
#  In Python, the zip() function is used to combine elements from multiple iterables (e.g., lists, tuples) into tuples. 
# It returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the input iterables. 
# The resulting iterator stops when the shortest input iterable is exhausted.

# in other words, takes the first item from the first list, takes the second item from the second list
# and puts them in a tuple together
# all lists must have the same number of items, otherwise, items that do not have a pair
# will be ignored

sample_list = [45, 12 , 11, 99, 12]
sample_second = [56, 34, 23, 11, 45]
print(list(zip(numbers, sample_list, sample_second))) # [(2, 45, 56), (4, 12, 34), (12, 11, 23), (22, 99, 11), (33, 12, 45)]


# reduce
# The reduce() function is part of the functools module in Python and is used to perform a cumulative operation on the items of an iterable, 
# from left to right, in a way that reduces the iterable to a single accumulated result. 
# It repeatedly applies a binary function to the items, accumulating the result.

# Yes, you can think of reduce() as a way to calculate a "total" or an "accumulated result" over all the items in an iterable. 
# It's a functional programming concept that helps reduce a sequence of values to a single value by successively applying a binary function.

def accumulator(acc :  int, item: int):
    return acc + item

from functools import reduce
print(reduce(accumulator, numbers, 0))