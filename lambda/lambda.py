# lambda expressions

# Lambda expressions, also known as lambda functions, are a concise way to create anonymous functions in Python. 
# An anonymous function is a function that is defined without a name. Lambda expressions are useful when you need 
# a small function for a short period of time and don't want to formally define a full function using the def keyword.

# inline, one-time use functions

# syntax: lambda param: func(param)
# syntax: lambda param: action(param)

numbers = [2, 4, 3, 1, 56]
print(list(map(lambda item: item *2, numbers))) # multiply by 2
print(list(filter(lambda item : item %2 != 0, numbers))) # find the odd numbers


# create an expression that will square the list
print(list(map(lambda item: item ** 2, numbers))) # square the list items

# list sorting
# sort the list of tuples
# based on the second value

a = [(0, 2), (4, 3), (9, 9) , (10, -1)]

def sort_list_tuples(value : list):
    
    # each of the items is a tuple
    # we need to access the second value 
    # of the tuple

    second_values = [] # create a list for the sercond values

    # grab the second 
    for item in value:
        if isinstance(item, tuple):
            second_values.append(item[-1])

    # sort the second values
    second_values.sort()
    
    reasemble = [] # create a new list to return
    for second in second_values:
        for item in value:
            if second in item: # check if the second value is found in the tuple and append to the new list
                reasemble.append(item)


    return reasemble

print(sort_list_tuples(a))

# better version using list comprehension
def sort_list_tuples(lst):
    # Extract second values using list comprehension
    second_values = [item[-1] for item in lst if isinstance(item, tuple)]

    # Sort the original list based on the second values
    sorted_list = sorted(lst, key=lambda x: x[-1])

    return sorted_list

print(sort_list_tuples(a))

# achieving the same result using lambda
a = [(0, 2), (4, 3), (9, 9) , (10, -1)]
a.sort(key=lambda x: x[1])
print(a)