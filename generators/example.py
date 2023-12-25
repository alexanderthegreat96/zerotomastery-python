# what is a generator?
# special kind of function
# that generates a sequence of
# values over time
# they are memory efficient
# used for large data sets

def make_list(num):
    result = []
    # range is a generator
    for i in range(num):
        result.append(i * 2)
    return result

# this stuff lives in memory
# it's pointing to a location 
# in memory
my_list = make_list(100)
print(my_list)


# generator
# it's iterable
# ramge is a generator

def generator_function(num):
    for i in range(num):
        yield i # yield i

# for item in generator_function(100):
#     print(item)

# this is really fast as the data is released 
# from memory with each iteration
def fib_gen(number : int):
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp = a
        a = b
        b = temp + b

# for number in fib_gen(100):
#     print(number)

# this takes ages to run
# sice the data is stored in memrory
def fig_gen_list(number : int) -> list:
    a = 0
    b = 1
    results = []
    for i in range(number):
        results.append(a)
        temp = a
        a = b
        b = temp + b
    return results


