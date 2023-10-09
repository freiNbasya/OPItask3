import unittest
from GetHistoryUsers import GetHistory

class Test(unittest.TestCase):
    def test_gettingOnline(self):
        path = "C:/Labs_Kse/OPI/task3OPI/main/Users_dataGetHist.csv"
        date = "09-10-2023 11:24:47"
        result = GetHistory(path, date)
        
        self.assertEqual(result, 3)
if __name__ == '__main__':
    unittest.main()