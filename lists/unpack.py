# list unpacking
# in other words
# pre-assign the return foor variables
# to the list indexes

first_name, middle_name, last_name = ["alex", "john", "dan"]
print(first_name, middle_name, last_name)

# in case we have no idea how many elements are in the list
# or we just want to assign variables to the first 4
# we give variable names
# then we add one more variable starting with *var_name
# the final variable with * will store the rest of the elements

# another cool trick to getting the last element
# is to add another variable after *var_name

a, b, c, d, *whatever_is_left, last_item = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh"]

print(a, b, c, d, whatever_is_left)

print(last_item)