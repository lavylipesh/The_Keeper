class Credentials:
    """
    class that generates new instaces of credentials
    """
    credentials_list
def __init__(self,account,username,password):
    '''
    __init__ method that helps us define properties for our objects
    '''
    self.account = account
    self.username = username
    self.password = password
def save_credentials(self):
    '''
    method that saves credentials objects into credential_list
    ''' 
    Credentials.credentials_list.append(self)
def  delete_credentials(self):
    """
    deletes credentials from the credentials_list
    """
    Credentials.credentials_list.remove(self) 
@classmethod
def search_credentials(cls,username):
    """
    method that takes in username and returns account that matches the username
    """
    for credentials in class credentials_list:
        if credentials.username ==  username:
            return True
    return False
@classmethod
def display_credentials(cls):
    '''
    method that returns the credentials_list
    '''
    return cls.credentials_list
