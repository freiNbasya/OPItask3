import unittest
import subprocess

class TestMyScript(unittest.TestCase):

    def test_script_with_valid_inputs(self):
        input = "7\n05ed4eae5-d93c-6b18-be47-93a787c83bcb\n"
        
        process = subprocess.Popen(["python", "main/Program.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout = process.communicate(input)
        results=stdout[0].split('\n')
        expected_output = "User deleted"
        self.assertEqual(results[5], expected_output)

if __name__ == "__main__":
    unittest.main()