import unittest
from main.UserPredict import GetPredictionUser

class Test(unittest.TestCase):
    def test_gettingOnline(self):
        path = "main/testPredictions.csv"
        date = "09-10-2023 11:24:47"
        id = "2fba2529-c166-8574-2da2-eac544d82634"
        tolerance = 0.5
        result = GetPredictionUser(path, id, date, tolerance)
        
        self.assertEqual(result, "User will be online")
if __name__ == '__main__':
    unittest.main()