import unittest
from main.buildReportsdif import build
from main.check_dataSet import check

class Test(unittest.TestCase):
    def test_average(self):
        path = "main/testAvg.csv"
        result_first = check(path)
        choices = "1 1 1 1 1"
        result = build(result_first, choices)
        
        self.assertEqual(result, 'Created report base')
if __name__ == '__main__':
    unittest.main()