print("Hello world!") # print stuff

# using input to take input from the program
# and assign it to a variable to print

name = input("What is your name, dude?") # this will store data from the user

# let's perform string congatenation using +
print("You told me that your name is " + name)


# as a general sidenote, eveythint in python is an object
# meaning that you can chain methods to it
# for example, let's make the name UPPERCASE using the .upper() method

print("I will make this uppercase: " + name.upper())