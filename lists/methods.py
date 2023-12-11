# list methods

my_list = [12,22,212,44,1212,33,22]
print(my_list)

# append
# adds a new elements inside the list
# at the end

my_list.append(999)
print(my_list)

# insert
# same thing as the other one
# but this one allows you to add data
# in a certain place

my_list.insert(2, 991) # adds 991 after the 2nd element
print(my_list)

# extend
# extends the list

my_list.extend([12,65,34,32]) # basically adds elements in bulk
print(my_list)

# removing elements
# using pop(index)

my_list.pop(0) # removes the first element
print(my_list) 

# empty an entire list
# use .clear()

my_list.clear()
print(my_list)

my_list.extend([65, 23, 45, 34, 12])
print(my_list)

# index method, which gives you the index
print(my_list.index(45)) # index number 2

# this also words with start, stop arguments
print(my_list.index(34, 0, 4)) # start from the begging but end at the 3rd element

# checking for existance of a value in a list

print(44 in my_list) # False

print("alex" in "one of the guys is alex") # true

# count how many times something is in a list

print(my_list.count(45)) # 1


# sorting stuff
# will sort in ascending order
my_list.sort()

print(my_list)

my_list.sort(reverse=True)

# sorts in descending order
print(my_list)

# another method of reversing the order
my_list.sort()
my_list.reverse()


# another sortinng procedure can be done using the sorted function
# sorted produces a new array
# as opposed to the other one 
# simply modifying the current one

print(sorted(my_list))

# to copy a list
print(my_list[:])

# slicing  a list

print(my_list[:3]) # takes the first 3
print(my_list[:-3]) # takes the last 3 -> in our case just 2

# generate a new list
# list(range(start, stop)) -> starting from and ending in
# list(range(stop)) -> ending in

print(list(range(1, 100)))
print(list(range(5)))

# joining elements from a list in a string

my_list_of_words = ["hello", "what's", "up", "dude"]
print(" | ".join(my_list_of_words))