is_young = True
is_licenced  = False
is_amateur = True
is_engineer = True


if is_young:
    if is_licenced and is_engineer:
        print("This guy has a bachelor's degree and is an engineer")
    elif is_amateur and is_engineer:
        print("He's an engineer, but he doesn't have a degree.")
    else:
        print("This guy isn't an engineer or he is but has no college degree")
else:
    print('He\'s just too old for this.')

# truthy and falsey
# a truthy or falsey value
# in python is basically any
# thing that returns True or False
# if you apply the bool() function to it

# is this a number?
print(bool(15))
print(bool(0))

# is this a string
print(bool(""))

# List of Falsey Values
falsey_values = [
    False,  # False constant
    0,      # Numeric zero
    None,   # None object
    "",     # Empty string
    [],     # Empty list
    (),     # Empty tuple
    set(),  # Empty set
    {},     # Empty dictionary
    # Custom objects with __bool__ or __len__ returning False or 0
    # (Note: Custom objects not explicitly shown in this example)
    # Other values evaluating to False in a boolean context
    # (Note: These may vary depending on the context and object)
]

# easiest way to showcase this example
# given 2 values

username = "username"
password = "password"

if bool(username) and bool(password):
    print("They filled the username and password")


# ternary operator
# inline true false
# shorthand expression in other languages

# condition_if_true if condition else  condition_if_false
# if username == alex, then username =  alex else it is equal to "no"

username = "alex" if username == "alex" else "No"
print(username)

# short circuiting
# In Python, short-circuiting refers to the behavior of logical operators (and and or) 
# that allow the interpreter to not evaluate the entire expression if the result can be 
# determined from part of it. This can be particularly useful for efficiency and 
# can also be leveraged for concise and expressive code.

is_friend = True
is_user = True

# as a general idea OR is more performant than AND
# this is due to short-circuiting
# in other words, it only evalues the first
# expression and then it skips the second one
# since either one of the results is ok

if is_friend or is_user:
    print("Yup")

# logical operators
# they control the flow

operators = ["and", "or", "not",  ">", ">=", "<=", "<", "!=", "=", "=="]
print(operators)

# exercise


is_magician = True
is_expert = False

if is_magician and is_expert:
    print("You are a master magician.")
elif is_magician and not is_expert:
    print("at least yolu are getting there") 
else:
    print("you need magic powers")

# is vs ==

print(True == 1) # true
print('1' == 1) # false, different data types
print([] == 1) # false, different data types
print(10 == 10.0) # true, even if different data types
print([] == []) # true since both lists are the same

# = -> checks for equality in value
# is -> checks if the location in memory is the same 
# The is operator is used to test if two variables refer
# to the same object in memory (i.e., they have the same identity).

print(True is True) # same place in memory
print('1' is 1) # false, it would need to be '1' for it to be true
print([] is 1) # false
print(10 is 10.0) # false, it would need to be 10
print([] is []) # false due to the fact that both lists are created in 2 different places
print([1, 2, 3] is [1, 2, 3]) # same thing as above