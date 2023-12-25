# error handling 2
# as a general observation
# use of type hinting is really good
# at preventing further errors in the code

def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError:
        print('Need numbers')

print(sum("asd", 3))

def type_hinted_sum(number1 : int, number2: int) -> int:
    return number1 + number2

try:
    print(type_hinted_sum("aaa", 23))
except TypeError as error:
    print(f'We need numnbers: {error}')