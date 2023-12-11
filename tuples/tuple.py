# tuple
# immutable structure
# similar to a list
# but no operations can be 
# performed directly

my_tuple = ("this", "element", "element", "here")
print(my_tuple)
print(my_tuple[2])

# use case is simple: the tuple storing whatever
# should not be changed

# it does support slicing too

print(my_tuple[0:2]) # took the first 2


# it does support unpacking as well
first, second, *whatever = my_tuple
print(first, second, whatever)

# couting is supported as well
print(my_tuple.count("element")) # will print 2

# supports index as well
print(my_tuple.index("element"))

# len is supported as well
print(len(my_tuple))