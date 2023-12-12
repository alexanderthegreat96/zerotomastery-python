# set is an unordered collection of unique objects
# the scope of using sets is to filter, arrange, pull stuff
# from lists or list like objects aka iterables
# they are mutable

my_set = {"this", "is", "something", "something", "weird"}
print(my_set)

# using this will help remove duplicated elements from lists
# or even tuples, granted, they will need to be converted to lists first

my_set.add("weird")
my_set.add("of course")

print(my_set)

#  practical example of removing duplicates from a list

my_list = [12, 12, 3, 43, 43, 89, 100, 101, 102, 202, 202]
print(set(my_list))

# it supports quite  a view methods

# .difference()
# .discard()
# .difference_update()
# .intersection()
# .isdisjoint()
# .issubset()
# .issuperset()
# .union()


# using .difference() method

set_a = {12, 22, 32, 44, 33, 16, 18}
set_b = {13, 22, 89, 44, 33, 13, 18}
print(set_b.difference(set_a)) # showcase which elements in set_b  and set_a are differente. in other words, it compares set_b with set_a
print(set_a.difference(set_b)) # showcase which elements in set_a  and set_a are differente. in other words, it compares set_a with set_b

# using the .discard() method
# similar to pop for lists and dicts and tuples
# removes an element from a set
# if it is a member
set_a.discard(33) # returns None 
print(set_a)

# using .difference_update() method
# removes the elements of another set from this one
# in other words, remove elements from set_b that belong to set_a
set_b.difference_update(set_a)
print(set_b)

# using .intersection_method()
# gives the intersection
# aka the common elements
print(set_b.intersection(set_a))

# using isdisjoint()
# returns True or False
# checks if common elements are found
print(set_a.isdisjoint(set_b)) # there are common elements, therefore True is returned

# using .union()
# basically combines both sets
# similar to list.extend()
print(set_a.union(set_b))

# using .subset()
# returns True or False
# and as the name suggests,
# is set_a a subset of set_b
# in other words, are the values from a
# inside b

print(set_a.issubset(set_b))

# .issuperset()
# returns True or False
# does set_a encopass set_b

print(set_a.issuperset(set_b)) # and no, it's not