import pyperclip
class Credentials:
    """
    class that generates new instaces of credentials
    """
    credentials_list = []
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
        for credentials in cls.credentials_list:
            if credentials.username ==  username:
                return credentials
        return False
    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials_list
        '''
        return cls.credentials_list
    @classmethod
    def test_credentials_exist(cls,username):
        '''
        checks if credentials exist from the credentials_list
        '''
        for credentials in cls.credentials_list:
            if Credentials.username == username:
                return True
            return False
    @classmethod
    def copy_password(cls,username):
        credentials_found = Credentials.search_credentials
        #pyperclip.copy(credentials_found.password)

