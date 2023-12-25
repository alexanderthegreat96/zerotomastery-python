# exception handling
# basically, error handling
try:
    age = int(input('What is your age? Type here:'))
    print(f'Your age is {age}')

except ValueError:
    # Handle the case where the input cannot be converted to an integer
    print("Error: Please enter a valid integer.")
except TypeError:
    # Handle the case where the type is incorrect
    print("Error: Unexpected data type.")
except Exception as e:
    # Handle other types of exceptions
    print("An unexpected error occurred:", e)
