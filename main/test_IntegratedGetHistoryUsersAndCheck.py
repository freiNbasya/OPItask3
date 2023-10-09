import unittest
from GetHistoryUsers import GetHistory
from check_dataSet import check

class Test(unittest.TestCase):
    def test_gettingOnline(self):
        path = "C:/Labs_Kse/OPI/task3OPI/main/Users_dataGetHist.csv"
        result_first = check(path)
        date = "09-10-2023 11:24:47"
        result = GetHistory(result_first, date)
        
        self.assertEqual(result, 3)
if __name__ == '__main__':
    unittest.main()