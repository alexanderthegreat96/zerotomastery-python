# do something
# do something
# do something

# when you break the flow
# you basically use certain
# conditions to direct
# your program to do something 
# else

def who_is_this(name : str):
    if name == "Alex":
        return "go_on"
    elif name == "George":
        return "go_on_again"
    else:
        return "stop_this"
    

if who_is_this("Alex") == "go_on":
    print("I should go on")