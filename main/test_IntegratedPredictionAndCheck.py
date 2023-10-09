import unittest
from Prediction import GetPrediction
from check_dataSet import check

class Test(unittest.TestCase):
    def test_gettingOnline(self):
        path = "C:/Labs_Kse/OPI/task3OPI/main/testPredictions.csv"
        result_first = check(path)
        date = "09-10-2023 11:24:47"
        result = GetPrediction(result_first, date)
        
        self.assertEqual(result, "Prediction 1")
if __name__ == '__main__':
    unittest.main()