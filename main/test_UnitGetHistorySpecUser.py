import unittest
from GetHistorySpecUser import GetHistorySpec

class Test(unittest.TestCase):
    def test_gettingOnline(self):
        path = "C:/Labs_Kse/OPI/task3OPI/main/Users_dataGetHist.csv"
        date = "09-10-2023 11:24:47"
        id = "8b0b5db6-19d6-d777-575e-915c2a77959a"
        result = GetHistorySpec(path, id, date)
        
        self.assertEqual(result, "User is online")
    def test_gettingOffline(self):
        path = "C:/Labs_Kse/OPI/task3OPI/main/Users_dataGetHist.csv"
        date = "09-10-2023 11:24:47"
        id = "5ed4eae5-d93c-6b18-be47-93a787c83bcb"
        result = GetHistorySpec(path, id, date)
        
        self.assertEqual(result, "User is offline last time seen online: ['09-10-2023 10:24:47']")
if __name__ == '__main__':
    unittest.main()