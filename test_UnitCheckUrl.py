import unittest
from main.checkUrl import check_Url

class Test(unittest.TestCase):
    def test_checkUrl(self):
        url = "https://sef.podkolzin.consulting/api/users/lastSeen"
        result = check_Url(url)
        
        self.assertEqual(result, url)
if __name__ == '__main__':
    unittest.main()