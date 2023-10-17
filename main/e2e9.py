import unittest
import subprocess

class TestMyScript(unittest.TestCase):

    def test_script_with_valid_inputs(self):
        input = "9\n5ed4eae5-d93c-6b18-be47-93a787c73bcb\n"
        
        process = subprocess.Popen(["python", "C:/Labs_Kse/OPI/task3OPI/main/Program.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout = process.communicate(input)
        results=stdout[0].split('\n')
        expected_output = "Average daily time for this user is 0 days 03:00:00, Average weekly time for this user is 0 days 03:00:00"
        self.assertEqual(results[5], expected_output)

if __name__ == "__main__":
    unittest.main()