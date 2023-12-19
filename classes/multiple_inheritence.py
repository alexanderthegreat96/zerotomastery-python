class User:
    __is_logged_in = False

    def __init__(self, username: str, password: str) -> None:
        self._username = username
        self._password = password

        if not self.__is_logged_in:
            self._login()

    def _login(self):
        print("Loggin in...")
        
    def _logout(self):
        if self.__is_logged_in:
            print("Logging out...")
        else:
            print("You gotta be logged in first to logout...")


class Admin(User):
    def __init__(self, username : str, password : str) -> None:
        super().__init__(username, password)

    def _can_ban(self):
        print (f'User {self._username} can ban!')
    
    def _can_unban(self):
        print(f'User {self._username} can unban!')
    

class Moderator(User):
    def __init__(self, username : str, password : str) -> None:
        super().__init__(username, password)

    def _can_mute(self):
        print(f'User {self._username} can mute')

    def _can_unmute(self):
        print(f'User {self._username} can unmute!')
    
class SuperUser(Admin, Moderator):
    def __init__(self, username: str, password: str) -> None:
        super().__init__(username, password)
    
superuser = SuperUser("alex", "alex")
superuser._can_ban()
superuser._can_unban()
superuser._can_mute()
superuser._can_unmute()

# as you can see, SuperUser inherits from both Admin and Moderator
# it has access to these methods