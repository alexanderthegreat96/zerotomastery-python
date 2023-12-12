# while loops
# it perpetually executes something
# as long as the condition is True

# while CONDITION: do something

found_user = False

while found_user:
    print("Analyzing...")


count = 0
while count < 50:
    count += 1
    print(count)
else:
    print("Done looping to 50")