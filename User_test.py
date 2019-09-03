import unittest
from User import User
class TestUser(unittest.TestCase):
     '''
     Test class that defines test cases for the user class behaviours.
     '''
     def setUp(self):
          '''
          set up method that runs before each test cases.
          '''
          self.new_user = User("pesh","1234")
     def test_init(self):
          '''
          test_init test case to test if the object is initialized properly
          '''
          self.assertEqual(self.new_user.username,"pesh")
          self.assertEqual(self.new_user.password,"1234") 
     def test_save_user(self):
          '''
          test to see if the user object has saved details
          '''
          self.new_user.save_user()
          self.assertEqual(len(User.user_list),1)
if __name__ =='__main__':
     unittest.main()           