# dict  -> dictionaries
# a.k.a map
# aka associative array
# aka hashtable
# it's a key value structure

# almost identical to JSON
# in terms of syntax
my_dict = {
    "first_name" : "alex",
    "last_name" : "lup",
    "age" : 27
}

print(my_dict)

# accesing data
print(my_dict["first_name"]) # how you access data

# very important
# a key within a dictionary needs to be immutable
# aka hashable

# valid types: bool, string, int, tuple

# a key in a dict has to be unique