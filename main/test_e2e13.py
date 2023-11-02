import unittest
from unittest.mock import patch
from Program import main
class E2E10(unittest.TestCase):
    @patch('builtins.input',
           side_effect=['13'])
    def test_printList(self, mock_input):
        result = main()
        self.assertEqual(result, 'Dataset successfuly printed')
if __name__ == '__main__':
    unittest.main()