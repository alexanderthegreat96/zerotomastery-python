from typing import Callable
import time
# every variable can be a function
# if it meets the criteriae
# this is a good example on how
# decorators will work

def hello(func):
    func()

def greet():
    print("Hello")

hello(greet)

# higher order function -> HOC
# can either be a function
# a function that accepts another function
# hello(func) -> HOC

# or a function that returns another function

def some_func() -> Callable[..., int]:
    def my_func():
        return 5

    return my_func

# we called some_func
mine = some_func()
# we called mine as a func
print(mine())

# a decorator supercharges a function
# it wraps around a function, can enhance or modify it

def alexander(func):
    def wrapper():
        print('*******') # runs before
        func() # executing the function
        print('*******') # runs after
    return wrapper


@alexander
def login():
    print("Loggin in...")

login()



# define the decorator

def control(func) -> Callable[..., None]:
    def wrap_around(*args, **kwargs):
        print("Control before...")
        result = func(*args, **kwargs)
        print("Control after...")
        return result
    return wrap_around

def benchmark(func: Callable) -> Callable:
    def wrap_around(*args, **kwargs):
        start = time.time() * 1000  # Convert seconds to milliseconds
        result = func(*args, **kwargs)
        end = time.time() * 1000

        elapsed_time = end - start

        print(f'Took {elapsed_time:.2f} milliseconds to execute {func.__name__}')

        return result

    return wrap_around

# let's deal with arguments
@control
def greeting(name : str = "Mike") -> None:
    print(f'Greetings, {name}. How was your day?')

greeting("Alexander")

@benchmark
def count_to(max_value : int) -> list:
    result = []
    for i in range(max_value):
        result.append(i)

    return result

count_to(9999)


@benchmark
def count_to_performance(max_value : int):
    numbers = []
    while max_value > 0:
        yield max_value
        numbers.append(max_value)
        max_value -= 1

    return numbers

list(count_to_performance(60000))

