import unittest
from unittest.mock import patch
from Program import main
class E2E10(unittest.TestCase):
    @patch('builtins.input',
           side_effect=['11'])
    def test_buildReports(self, mock_input):
        result = main()
        self.assertEqual(result, 'printed reports')
if __name__ == '__main__':
    unittest.main()