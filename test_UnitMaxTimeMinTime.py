import unittest
from main.MaxTimeMinTime import maximumTime
from main.MaxTimeMinTime import minimumTime

class Test(unittest.TestCase):
    def test_maximumTime(self):
        path = "main/testAvg.csv"
        id = "5ed4eae5-d93c-6b18-be47-93a787c73bcb"
        result = maximumTime(path, id)
        
        self.assertEqual(result, 3600.0)
    def test_minimumTime(self):
        path = "main/testAvg.csv"
        id = "5ed4eae5-d93c-6b18-be47-93a787c73bcb"
        result = minimumTime(path, id)
        
        self.assertEqual(result, 3600.0)
if __name__ == '__main__':
    unittest.main()