import unittest
from avg import average

class Test(unittest.TestCase):
    def test_average(self):
        path = "C:/Labs_Kse/OPI/task3OPI/main/testAvg.csv"
        id = "5ed4eae5-d93c-6b18-be47-93a787c73bcb"
        result = average(path, id)
        
        self.assertEqual(result, 'Average daily time for this user is 0 days 03:00:00, Average weekly time for this user is 0 days 03:00:00')
if __name__ == '__main__':
    unittest.main()