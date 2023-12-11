# generalization of numbers 
# to showcase math operations and
# float / int


print(type(6)) # int
print(type(2 - 4))  # -2, negative numbers are also integers
print(type(2 * 4)) # 8, int
print(type(2 / 4)) # 0.5 which is a float
print(type(5.213423)) # 5.213423 still a float regardless of how many decimal points 
print(type(0)) # still an int
print(type(10 + 1.2)) # 11.2, will be automatically converted to float

print(2 ** 5) # ** -> the power of -> 2 to the power of 5 is 32 -> int
print(2 // 4) # returns 0, this  // is the floor division, this doesn't account for the fractional part -> int
print(2 / 4) # returns 0.5 as it accounts for the fractional part -> float

# returns 1. this is a modulo operator, returns the remainder of the division of the left operand to the right
# since 4 goes into 5 once with a remainder of 1
print(5 % 4) # 1
print(6 % 3) # 0, because 3 goes into 6 zero times


# complex numbers
print(complex(12))

# binary
print(int(bin(12), 2)) # take the binary equivalent, convert it to an int with the base 2