# dictionary comprehensiom

some_dict = {
    "key": 1,
    "value": 2
}

my_dict = {key:value**2 for key, value in some_dict.items() if value %2 == 0}
print(my_dict)


# another example
# basically key:value for value in list
#           number: number*2 for number in list

my_other = {number:number*2 for number in [2, 3, 6, 7, 10]}
print(my_other)

# basically creates a dictionary by using each number in the range
# key is number, value is number * 3
another_big = {number : number *3 for number in range(100)}
print(another_big)