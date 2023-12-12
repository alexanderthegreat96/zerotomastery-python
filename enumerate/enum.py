
# In Python, enumerate is a built-in function that allows you to iterate
# over a sequence (such as a list, tuple, or string) along with its index. 
# It returns pairs of index and corresponding element during each iteration. 
# enumerate function
# similar behaviour as range

# syntax: enumerate(any, start_index)

for i, char in enumerate('hellllllooo', 1):
    print(i, char)


for index, number in enumerate(list(range(1, 101))):
    if number == 50:
        print(f'The index of 50 is {index}')