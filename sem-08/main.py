from entities import Character
from errors import *

class Menu:
    def print_menu(self):
        print("1. Create a new character")
        print("2. Create a weapon of exist character")
        print("3. Create extra object of exist character")
        print("4. Print all heroes")
        print("5. Delete exist character")
        print("Exit")

    def command_create_character(self, name, sex, ch_class):
        pass

    def run(self):
        # infinite menu loop
        while True:  
            # print the menu
            # ...

            # ask the user to choose a command
            self.print_menu()
            choice = input("Choose an item from the menu: \n> ")
            # catch errors
            try:
                # process the user's choice
                if choice == "1":                    
                    # ask the user to input the necessary command parameters
                    name = input("Enter the character name (alpha-numeric): ")
                    character = self.command_create_character

                elif choice == "2":
                    name = input("Enter the weapon name (alpha-numeric): ")
                    if len(name) < 4 or not name.isalpha():
                        raise InvalidDataFormat("Invalid name")
                    attack = input("Points of attack: ")
                elif choice == "3":
                    name = input("Enter the object name (alpha-numeric): ")
                    if len(name) < 4 or not name.isalpha():
                        raise InvalidDataFormat("Invalid name")
                else:
                    raise InvalidCommand("Error: Invalid choice")
            except Exception as ex:
                print(f"Error: {str(ex)}")
            
            print()

if __name__ == '__main__':
    menu = Menu()
    menu.run()
