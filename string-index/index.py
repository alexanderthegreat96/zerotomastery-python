# since everything in python is an object
# we can access individual parts of the strings
# by giving it an index
# sort of like the same way it works with lists
index = "hello, motherfucker!"
print(index[0]) # prints h

# usage of indexes in lists
my_list = [12, 23, 22, 33]
print(my_list[1]) # prints 23

# usage of indexes in tuples (immutable lists)
my_tuple = tuple(my_list)
print(my_tuple[1]) # will print 23


# accessing values using [start:stop]
print(index[:3]) # prints hel
print(index[3:]) # skips the first 3 keys and prints the rest
print(index[4:8]) # takes stuff in between 4 and 8
print(index[0:4:6]) # takes first, skipps, goes to the 4 and 6
print(index[-1]) # takes the last element
print(index[:-6]) # takes everything up untill 6
print(index[::-1]) # reverses the order


# strings are immutabke
# meaning that you cannot assign data on the fly

# assigning a key and a value won't wory
# instead, we need to glue the character or word. /  concatenate it

# wont work
# index[-1 + 1] = "Word"
# will work

index = index + " how the hell are you?"
print(index)