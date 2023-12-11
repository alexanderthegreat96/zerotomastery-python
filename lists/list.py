import random
# list is basically an array containing a slice of values
my_list = ["this", "list", "contains", "stuff", 1, 2, True]
print(my_list)

# matrix
# fancy name for lists
# that contain other lists
# with equal structures

my_matrix = [
    [1, 2 ,3],
    [6, 5, 4],
    [5, 2, 2]
]

# this will generate a matrix
def generate_matrix(numbers : int = 5, rows: int = 10) -> list:
    matrix = []

    for row in range(0, rows):
        row = []
        
        for time in range(0, numbers):
            row.append(random.randint(1, 999))

        matrix.append(row)
    
    return matrix

print(generate_matrix(3, 3))