# set is an unordered collection of unique objects
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