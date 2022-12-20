 # User
class InvalidUserData(Exception):
    def __init__(self, message = "Enter valid data", *args: object) -> None:
        super().__init__(message, *args)

class UserNotFound(Exception):
    def __init__(self, message="This user doesn't exist", *args: object) -> None:
        super().__init__(message, *args)

class UserAlreadyExists(Exception):
    def __init__(self, message = "User already exists", *args: object) -> None:
        super().__init__(message, *args)

class UserAlreadyOwnsAccount(Exception):
    def __init__(self, message="This user already has an account", *args: object) -> None:
        super().__init__(message, *args)

# Account 
class AccountNotFound(Exception):
    def __init__(self, message="Account not found", *args: object) -> None:
        super().__init__(message, *args)

class UnsufficientBalance(Exception):
    def __init__(self, message="Not enough money", *args: object) -> None:
        super().__init__(message, *args)

class InvalidAccountData(Exception):
    def __init__(self, message="Invalid data", *args: object) -> None:
        super().__init__(message, *args)

class InvalidAccountType(Exception):
    def __init__(self, message="Invalid type", *args: object) -> None:
        super().__init__(message, *args)

# Menu
class InvalidMenuChoice(Exception):
    def __init__(self, message="You've chosen a wrong number", *args: object) -> None:
        super().__init__(message, *args)
