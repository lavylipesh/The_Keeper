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
    def create_user():
        '''
        method thhat helps us create our user
        '''        
    def save_user(self):
        '''
        method that saves user objects into user_list
        ''' 
        User.user_list.append(self)
    def generatePassword():
        return ' '.join(random.choice(string.ascii_letters + string.digits) for i in range (10))
    
