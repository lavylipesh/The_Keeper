#!/usr/bin/env python3.6
from User import User
from credentials import Credentials
def keep():              
    print(" _      __       ____________    _________       __________         ")
    print("| |    / /    | |___________|  | |________|      | |         \ ")
    print("| |   / /     | |              | |               | |________  \ ")
    print("| |  / /      | |              | |               | |        |  \  ")
    print("| | / /       | |              | |               | |        |   \ ")
    print("| |/ /        | |___________   | |________       | |________|   / ")
    print("| | \ \       | |___________|  | |________|      | |__________ /     ")
    print("| |  \ \      | |              | |               | |              ")
    print("| |   \ \     | |              | |               | |               ")
    print("| |    \ \    | |              | |               | |               ")
    print("| |     \ \   | |___________   | |_________      | |                ")
    print("|_|      \_\  | |___________|  |_|_________|     |_|                ")
keep()   


def create_user(username,password):
    '''
    fuction that creates user accounts
    '''
    new_user = User(username,password)
    return new_user
def save_user():
    '''
    a function to save a user
    '''
    User.save_user()
def generatePassword():
    '''
    function to generate a password for the user
    '''
    print(User.generatePassword())
     
def  create_credentials(account,username,password):
    '''
    function that creates new credentials
    '''

    new_credentials = Credentials(account,username,password)
    return new_credentials
def save_credentials():
    '''
    function that saves all our created credentials
    '''
    Credentials.save_credentials()
def delete_credentials():
    '''
    function to delete credentials
    '''
    credentials.delete_credentials()
def search_credentials():
    '''
    functio that finds credentials by username and returns the credentials
    
    '''
    return Credentials.search_credentials()
def test_credentials_exist():
    '''
    function that checks if credentials exist
    '''
    return Credentials.test_credentials_exist()
def display_credentials():
    '''
    function that returns all saved credentials
    '''
    return Credentials.display_credentials()
def main():
    print("HELLO ;)")
    print('*'*100)
    print("Welcome to KEEPER \n You can store passwords for all your existing accounts and generate passwords for any account you may want to sign in to.\n ENJOY!!!")
    print("*"*100)
    print("To access keeper please login")
    print("Username:")
    username = input()
    print('*'*20)
    while True:
        print("use the shortcodes:'pass' to create your password\n'gp' to generate your password")
        my_choice = input()
        if my_choice == 'pass':
            print("Your password Please")
            password = input()
            print('*'*60)
            print(f"Welcome to Keeper {username} your password is {password}")
        elif my_choice == 'gp':
            password = generatePassword()
            print('*'* 80)
            print(f"Welcome to Keeper {username} your password is {password}")
        else:
            print("INVALID!!!!!!")
            print('')
        my_choice = input().lower()
    print('')
    
    while True:
        print("Use the shortcodes: 'MC'-to make new credentials,'delete'-to delete unwanted credentials,'SC'-to see credentials\n 'EXIT!!'to exit Keeper")
        if short_code == 'MC':
            print("Which account details would you like to save??")
            account == input()
            print("Enter your Username")
            username == input()
            while True:
                print("use the shortcodes:\n 'pass' to create your own password \n 'gp' for the application to generate a password for you")
                if short_code == 'pass':
                    print("Please input your password")
                    password == input()
                elif short_code ==  'gp':
                    password == generatePassword()
                    print('*'*70)    



        

if __name__ == '__main__':
    main()                              
