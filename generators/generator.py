
# The yield statement is used in Python to create a generator function. A generator is a special type of iterator
# that allows you to iterate over a potentially infinite sequence of values without the need to store them all in 
# memory at once. It's particularly useful when dealing with large datasets or when generating values on-the-fly.

def generate_numbers(end_at : int = 10):
    current = 0
    while current <= end_at:
        yield current
        current += 1


for number in generate_numbers(20):
    print(number)

# using for
def squares_generator(n):
    for i in range(n):
        yield i ** 2

for square in squares_generator(5):
    print(square)

# generate fibbonaci numbers
def fibonacci_generator(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

for number in fibonacci_generator(10):
    print(number)