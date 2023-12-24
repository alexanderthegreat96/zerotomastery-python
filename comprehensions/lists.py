# 
# Python comprehensions are concise and expressive ways to create data structures (lists, dictionaries, sets) in a single line of code. 
# They provide a more readable and often more efficient alternative to using traditional loops. There are three types of comprehensions in Python:


# Creates a new list by applying an expression to each item in an existing iterable (list, tuple, string, etc.).
squares = [x**2 for x in range(10)]
print(squares)

numbers = [num*2 for num in range(50)]
print(numbers)

# you can also add conditions within [] at the end of the expression
# so you can actually do something
multiletter = [letter for letter in "this is the greates of all time".replace(" ","") if letter != "t"] # will return a list of letters except for t 
print(multiletter)

# maing a list of letters from a word
letters = [letter for letter in "alexandru"]
print(letters)

reversed_letters = [letter for letter in "alexandru"][::-1]
print(reversed_letters)


# excerise comprehension duplicates
some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]

duplicates = list(set([letter for letter in some_list if some_list.count(letter) > 1]))
print(duplicates)