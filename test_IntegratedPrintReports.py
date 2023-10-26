import unittest
from main.printReports import printReports
from main.check_dataSet import check

class Test(unittest.TestCase):
    def test_average(self):
        path = "main/reportDataBase.csv"
        result_first = check(path)
        result = printReports(result_first)
        
        self.assertEqual(result, 'printed reports')
if __name__ == '__main__':
    unittest.main()