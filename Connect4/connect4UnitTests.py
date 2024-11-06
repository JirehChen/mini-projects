'''
Unit Tests for connect4.py
Jireh Chen, 6th Nov 2024
'''

from connect4 import *
import unittest
from unittest.mock import patch, Mock

class UnitTesting(unittest.TestCase):

    @patch('builtins.input')
    def test_welcome(self, mocked_input):
        mocked_input.side_effect = ["John", "Jane"]
        results = welcome(["",""])
        self.assertEqual(results, ["John", "Jane"])


if __name__ == "__main__":
    unittest.main()
