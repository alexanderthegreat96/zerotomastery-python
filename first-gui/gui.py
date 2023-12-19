import random
def generate_matrix(numbers : int = 5, 
                    rows: int = 10, 
                    min_number : int = 1, 
                    max_number : int  = 999) -> list:
    matrix = []

    for row in range(0, rows):
        row = []
        
        for time in range(0, numbers):
            row.append(random.randint(min_number, max_number))

        matrix.append(row)
    
    return matrix

def build_gui(data : list):
    for item in data:
        if isinstance(item, list):
            build_gui(item)
        else:
            if item == 3:
                print("*-*", end=" ")
            
            if item == 2:
                print("|/", end=" ")
    
            if item == 1:
                print("*", end=" ")

            if item == 0:
                print("", end=" ")
            
            

matrix = generate_matrix(5, 10, 0, 3)
build_gui(matrix)