
# given the same input it returns the same output
# produces no side effects as it doesn't modify stuff 
# globally

def multiply_by2(li : list):
    new = []
    for item in li:
        new.append(item * 2)
    return new

print(multiply_by2([1, 2, 3]))
