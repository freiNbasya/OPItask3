import unittest
from main.totalTime import totalTime
from main.check_dataSet import check

class Test(unittest.TestCase):
    def test_removingUser(self):
        path = "main/testTotatTime.csv"
        result_first = check(path)
        id = "5ed4eae5-d93c-6b18-be47-93a787c73bcb"
        result = totalTime(result_first, id)
        
        self.assertEqual(result, 'Total time for this user is 10800.0')
if __name__ == '__main__':
    unittest.main()