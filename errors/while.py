while True:
    try:
        age = int(input('What is your age? Type here:'))
        print(f'Your age is {age}')
        age / 10
    except ValueError:
        print('Need a number. Try again...') # when it hits here, it goes back up to try
    except TypeError:
        print('Need a valid integer.')
    except ZeroDivisionError:
        print('Give me a number that is higher than 0')
    else:
        print('Going out...') # this is in case everything goes well
        break