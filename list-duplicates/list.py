# checking for duplicates
my_list = ["a", "b", "b", "c", "c", "d", "e", "f", "g"]

# removing duplicate values
filtered = list(set(my_list))
filtered.sort()
print(filtered)

# let's find the duplicates
duplicate_values = []
for item in my_list:
    if my_list.count(item) > 1:
       if item not in duplicate_values:
            duplicate_values.append(item)

print(duplicate_values)