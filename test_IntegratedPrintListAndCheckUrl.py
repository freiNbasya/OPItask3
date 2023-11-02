import unittest
from main.PrintList import printList
from main.checkUrl import check_Url

class Test(unittest.TestCase):
    def test_printList(self):
        url = "https://sef.podkolzin.consulting/api/users/lastSeen"
        result_first = check_Url(url)
        result = printList(result_first)
        
        self.assertEqual(result, 'Dataset successfuly printed')
if __name__ == '__main__':
    unittest.main()