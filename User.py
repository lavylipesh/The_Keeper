import string
import random
class User:
    """
    class that generates new instances of users
    """
    user_list = []
    def __init__(self,username,password):
        '''
        __init__ method that helps us define properties for our objects
        '''
        self.username = username
        self.password = password    
    def save_user(self):
        '''
        method that saves user objects into user_list
        ''' 
        User.user_list.append(self)
    def generatePassword(num):
        password = ''
        for n in range(num):
            x = random.randint(0,100)
            password += string.printable[x]
        return password
    
