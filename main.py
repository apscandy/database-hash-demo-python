from database_utils import *
from hashing import *
import os 

username = "linus"
password = "Hello world"


def main():
    """Dispaly system"""
    while True:
        print("PLease select an option")
        print("Enter 1 to add a user to the database")
        print("Enter 2 to find a user in the database")
        print("Enter 3 to login")
        print("Enter 4 to list all")
        print("Enter 5 to delete the database tables")
        print("Enter 6 to exit the program")
        option = input(">$ ")
        clear_terminal()
        option_check(option)
        

def clear_terminal()->None:
    """Clears the terminal for a clean output"""
    if os.name == 'nt': os.system("cls")
    elif os.name == 'posix': os.system("clear")


def option_check(option):
    """Menu system"""
    if option == "6":
        clear_terminal()
        os.sys.exit(1)
    elif option == "5":
        database_delete_all()
        print("database deleted \n\n")
    elif option == "4":
        print(database_list_all())
        print()
    elif option == "3":
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        print(login(username, password))
    elif option == "2":
        username = input("Please enter a user you wish to follow: ")
        clear_terminal()
        print(database_find_user(username), "\n\n")
    elif option == "1":
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        database_add_user_salt_and_pepper(username, password)
        print("user added... \n\n")
    else:
        print("Please enter a valid option!!! \n\n")
        main()

def login(username, password):
    """Front end login system"""
    database_hash = database_find_user_password(username)
    database_salt = database_find_user_salt(username)
    valid = salt_hash_check(password, database_hash, database_salt)
    if valid:
        return "Yay you are logged in \n\n"
    else:
        return "Please try again \n\n"






















if __name__ == "__main__":

    #database_add_user_salt_and_pepper(username, password)
    #print(database_find_user(username))
    #print(database_find_user_password(username))
    #print(hash_check('Hello', str(database_find_user_password(username)[0])))
    #print(salt_generator())
    #print("\n"+database_list_all()+"\n")
    #print(database_user_login("andrew", "Hello"))
    #print(hash_password(password))
    #print(database_find_user_salt(username))
    #user_pass = database_find_user_password(username)
    #user_salt = database_find_user_salt(username)
    #print(salt_hash_check(password, user_pass, user_salt))
    #database_delete_all()
    #print(hash_password("passw0rd"))
    main()