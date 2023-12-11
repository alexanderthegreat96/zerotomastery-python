# variables hold DATA of a certain TYPE
# or at least they should

# snake_case
my_name = "alex"

print(type(my_name)) # str
# print(my_name + 12) # print can only print a certain data type at a single point in time
my_mix_var = "alex" + str(12) # this will print as it's converted to string


# augmented assignment operator
# long ass word that works similar to concatenation
# this works with multiplcations or any math operation too
number = 12
number += 1
number += 10

# keep adding data to the variable
print(number)

# works for strings as well

final = ""
names = ["alex", "is", "so", "fucking", "cool"]
for name in names:
    
    if name == names[-1]:
        final += name
    else:
        final += name + "_"
    
print(final)