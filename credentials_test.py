from credentials import Credentials
class TestCredentials(unittest.TestCase):
    '''
    a class that defines test cases for the credentials class behaviours
    '''
def setUp(self):
    '''
    Set up method to run before each test cases.
    '''
    self.new_credentials = Credentials("skype","pesh","1234")
def test_init(self):
    '''
    test case to check object initialization
    '''
    self.assertEqual(self.new_credentials.account,"skype")
    self.assertEqual(self.new_credentials.username,"pesh")
    self.assertEqual(self.new_credentials.password,"1234")
def save_credentials(self):
    '''
    test to see if the credential objects have been saved
    '''
    self.new_credentials.save_credentials()
    self.assertEqual(len(Credentials.credentials_list),1)
def tearDown(self):
    '''
    the method that does clean up after each test has been run.
    '''
    Credentials.credentials_list = []        

def test_save_multiple_passwords(self):
    '''
    test to check if we can save multiple passswords
    '''
    self.new_credentials.save_credentials()
    test_credentials = Credentials("skype","pesh","1234")
    test_credentials.save_credentials()
    self.assertEqual(len(credentials_list),2)
def test_delete_credentials(self):
    '''
    test to check if we canremove account 
    '''
    self.new_credentials.save_credentials()
        test_credentials = Credentials("skype","pesh","1234")
        test_credentials.save_credentials()

        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
def test_search_credentials(self):
        """
        test to see if we can find information by entering username
        """
        self.new_credentials.save_credentials()
        test_credentials = Credentials("skype","pesh","1234") 
        test_credentials.save_credentials()

        found_credentials = Credentials.search_credential("pesh")

        self.assertEqual(found_credentials.username,test_credentials.username)

def test_credentials_exist(self):
        """
        test to check if we can return a boolean if we cannot find the credentials.
        """
        self.new_credentials.save_credentials()
        test_credentials = Credentials("skype", "pesh", "1234")  
        test_credentials.save_credentials()
        credentials_exists = Credentials.credentials_exist("pesh")
        self.assertTrue(credentials_exists)

def test_display_credentials(self):
        '''
        method that displays all the credentials
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

if __name__ == '__main__':
    unittest.main()   

