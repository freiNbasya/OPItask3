import unittest
from main.buildReportsdif import build



class Test(unittest.TestCase):
    def test_average(self):
        path = "main/testAvg.csv"
        choices = "1 1 1 1 1"
        result = build(path, choices)
        
        self.assertEqual(result, 'Created report base')
if __name__ == '__main__':
    unittest.main()