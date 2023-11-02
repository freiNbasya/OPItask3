import unittest
from main.PrintList import printList

class Test(unittest.TestCase):
    def test_printList(self):
        url = "https://sef.podkolzin.consulting/api/users/lastSeen"
        result = printList(url)
        
        self.assertEqual(result, 'Dataset successfuly printed')
if __name__ == '__main__':
    unittest.main()