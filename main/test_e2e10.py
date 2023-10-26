import unittest
from unittest.mock import patch
from Program import main
class E2E10(unittest.TestCase):
    @patch('builtins.input',
           side_effect=['10', '1 1 1 1 1'])
    def test_buildReports(self, mock_input):
        result = main()
        self.assertEqual(result, 'Created report base')
if __name__ == '__main__':
    unittest.main()