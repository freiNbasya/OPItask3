import unittest
from main.avg import average
from main.check_dataSet import check

class Test(unittest.TestCase):
    def test_average(self):
        path = "main/testAvg.csv"
        result_first = check(path)
        id = "5ed4eae5-d93c-6b18-be47-93a787c73bcb"
        result = average(result_first, id)
        
        self.assertEqual(result, 'Average daily time for this user is 0 days 03:00:00, Average weekly time for this user is 0 days 03:00:00')
if __name__ == '__main__':
    unittest.main()