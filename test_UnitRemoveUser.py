import unittest
from main.removeUser import removeUser

class Test(unittest.TestCase):
    def test_removingUser(self):
        path = "main/testRemoveUser.csv"
        id = "05ed4eae5-d93c-6b18-be47-93a787c83bcb"
        result = removeUser(path, id)
        
        self.assertEqual(result, "User deleted")
if __name__ == '__main__':
    unittest.main()