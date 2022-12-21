class InvalidCommand(Exception):
    def __init__(self, message = "Invalid menu choice"):
        super().__init__(message, *args)
class InvalidDataFormat(Exception):
    def __init__(self, message = "Invalid data format"):
        super().__init__(message, *args)
class CharacterExists(Exception):
    def __init__(self, message = "Character already exists"):
        super().__init__(message, *args)
class InvalidCharacterClass(Exception):
    def __init__(self, message = "Invalid character fields"):
        super().__init__(message, *args)
class CharacterNotFound(Exception):
    pass
