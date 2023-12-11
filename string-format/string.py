# formatted string

# similar to string concatenation
# also similar to fmt.Printf in go

my_name = "Alexander"
my_age = 23
my_ocupation = "hacker"

# first way

print("Hello, " + my_name + ", you are:", str(my_age) + " and you are a " + my_ocupation)

# using print(f'')
# this automatically performs string conversion

print(f'Hello, {my_name}. You are {my_age} and you are a {my_ocupation}')

my_dict = {"women": "readhead", "cup": "D"}

print(f'Hello, {my_name}. You are {my_age} and you are a {my_ocupation}. You like {my_dict}')

# a different way of doing this
print('Hello, {}, you are {} and you like {}'.format(my_name, my_age, my_dict))

# string methods https://www.w3schools.com/python/python_ref_string.asp

print("hello dude".upper())
print("hello dude".replace("dude", "man"))
