
import utils.user_manager
import utils.dice_game
import utils.score

class Menu():
    def __init__(self): 
        pass

    def menu(self):
        print("Welcome to dice game!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = int(input("Please choose an option: "))

        if choice == 1:
            utils.user_manager.register()
        elif choice == 2:
            utils.user_manager.login()
        elif choice == 3:
            return
        
if __name__ == "__main__":
    Menu()

