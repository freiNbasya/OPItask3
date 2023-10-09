import unittest
from UserPredict import GetPredictionUser
from check_dataSet import check

class Test(unittest.TestCase):
    def test_gettingOnline(self):
        path = "C:/Labs_Kse/OPI/task3OPI/main/testPredictions.csv"
        result_first = check(path)
        date = "09-10-2023 11:24:47"
        id = "2fba2529-c166-8574-2da2-eac544d82634"
        tolerance = 0.5
        result = GetPredictionUser(result_first, id, date, tolerance)
        
        self.assertEqual(result, "User will be online")
if __name__ == '__main__':
    unittest.main()