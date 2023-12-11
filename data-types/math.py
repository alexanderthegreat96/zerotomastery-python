import math

# math functions
print(math.floor(33.3)) # it's the reverse of the function below
print(round(10.7)) # rounds to the closest decimal point
print(abs(-22)) # absolute number, aka no negative numbers

print(math.factorial(12)) # returns a factorial number

# tons of them: https://docs.python.org/3/library/math.html


# operator precendence, aka your basic math operator precedence

# first compute stuff from paranthesis
# power of **
# then multipliers
# then additions and substractions

print(abs(10 - 9 * 2)) # should give -8 but used abs and it returns 8