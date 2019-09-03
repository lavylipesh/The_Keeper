#!/usr/bin/env python3.6
from User import User
from credentials import Credentials
def keep():              
    print(" _      __       ____________    ___________      __________         ")
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
    function to create a new user
    '''
    #new_user = User(username,password):
    return new_user
def save_user(user):
    '''
    a function to save a user
    '''
    User.save_user()
def  create_credentials(account,username,password):
    '''
    function that creates new credentials
    '''
    #new_credentials = Credentials(account,username,password):
    return new_credentials
def save_credentials(credentials):
    '''
    function that saves all our creaated credentials
    '''
    Credentials.save_credentials()
def delete_credentials(credentials):
    '''
    function to delete credentials
    '''
    credentials.delete_credentials()
def search_credentials(username):
    '''
    functio that finds credentials by username and returns the credentials
    '''
    return Credentials
def test_credentials_exist(username):
    '''
    function that checks if credentials exist
    '''
    return Credentials
def display_credentials():
    '''
    function that returns all saved credentials
    '''
    return Credentials.display_credentials()
