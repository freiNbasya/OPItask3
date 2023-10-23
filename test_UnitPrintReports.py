import unittest
from main.printReports import printReports



class Test(unittest.TestCase):
    def test_average(self):
        path = "main/reportDataBase.csv"
        result = printReports(path)
        
        self.assertEqual(result, 'printed reports')
if __name__ == '__main__':
    unittest.main()