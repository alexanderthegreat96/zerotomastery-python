# a way to wrap stuff around a function in python
# args -> varioable number of arguments
# kwards -> variable number of key => value arguments
# ex: my_args_name : str = "whatewver"
def alex(func):
    def wrapper(*args, **kwargs):
        print("before")
        function_returns = func(*args, **kwargs)
        print("after")
        return function_returns
    return wrapper


@alex
def multiply(x : int, y : int) -> float:
    return x * y


print(multiply(12, 5))

# using variable args
def add(*args : int):
    result = 0
    for number in args:
        result += number

    return result

print(add(12, 12, 56))

# using keyword arguments
def print_stuff(**kwargs : any):
    for key, value in kwargs.items():
        print (key, value)

print_stuff(name="Alex", age = 27, job="engineer")

# functions are first class citizens