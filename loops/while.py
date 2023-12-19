# while loops
# it perpetually executes something
# as long as the condition is True

# while CONDITION: do something

found_user = False

while found_user:
    print("Analyzing...")

# using else
count = 0
while count < 50:
    count += 1
    print(count)
else:
    print("Done looping to 50") # this works like a break statement


# use cases
# while vs for loop
something = [12, 1232, 1221, 11]
for item in something:
    print(item)

# same way of doing the same thing
# normally, for is more visible
i = 0
while i < len(something):
    print(something[i])
    i += 1

# for simple loops, for is great
# for complex loops, while is better
# the most used case is for continous execution

# while True:
#     res = input("Say something my guy: ")
#     if res == "hi":
#         break

# break, continue, pass

# yes it works in for loops as well
for name in ["jasmin", "joe", "joey", "alex"]:
    if name == "alex":
        break
    print(name)

# as a general idea, break exists the current closing loop
# continue re-runs the current closing loop

for car in ["audi", "ford", "bmw", "chevrolet"]:
    print(car)
    if car == "bmw":
        break
    else:
        continue

# pass, does nothing
# it's generally used for code that needs to be implemented
def my_func(name : str = "Alex"):
    pass