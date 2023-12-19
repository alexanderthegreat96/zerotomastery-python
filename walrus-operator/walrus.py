# walrus operator

'''
The "walrus operator" is a feature introduced in Python 3.8, represented by the := syntax. 
Its official name is the "assignment expression." The walrus operator allows you to assign a value to a variable as part of an expression. 
It's called the "walrus operator" because the := symbol resembles the eyes and tusks of a walrus.
'''

# it's identical with what Go is doing with it

my_string  = "hi, there, what's up?"
if len(my_string) > 10:
    print("This is too long")

while (n := len(my_string) > 1):
    print(n)
    my_string = my_string[:-1]