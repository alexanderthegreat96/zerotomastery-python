# methods

my_dict = {
    "first" : 1,
    "last": 3,
    "something" : "else"
}

# .get() method will get a value by key
# in addition to that
# it can provide an exception being thrown 
# when the key doesn't exist
# or even set a default value if the key
# exists, but the value is none

print(my_dict.get("last"))


print(my_dict.get("some_key", "default value"))

# check if a value is in either keys or values

print("something" in my_dict)
print("Yes" if "something" in my_dict else "Nope")

# check only in keys

print("yes" if "something" in my_dict.keys() else "Nope")

#check only in values
print("Yes" if "something" in my_dict.values() else "Nope")

# using .items() method will return a tuple

print(my_dict.items())

# to iterate
for key, value in my_dict.items():
    print(key, value)


# make a copy of the list
another_dict = my_dict.copy()

print(another_dict)

# to delete data from a dict
my_dict.clear()
print(my_dict)

# wipe a key value pair
another_dict.pop("first")
print(another_dict) # takes as argument a key


# update / add data
another_dict.update({"this" : "that"})
print(another_dict)