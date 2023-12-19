
# by inheriting from list
# we can alter it's behaviour

class SuperList(list):
    def __init__(self) -> None:
        pass

    def __len__(self) -> int:
        print("Counting")
        return super().__len__()

    
my_list = SuperList()
my_list.append([12, 12, 122, 222, 33])
print(len(my_list))