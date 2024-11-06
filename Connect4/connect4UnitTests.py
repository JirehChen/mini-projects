'''
Unit Tests for connect4.py
Jireh Chen, 6th Nov 2024
'''

from connect4 import *
import unittest
from unittest.mock import patch, Mock

class UnitTesting(unittest.TestCase):

    @patch('builtins.input')
    def test_namePlayers(self, mocked_input):
        mocked_input.side_effect = ["John", "Jane"]
        results = Connect4()._namePlayers(["",""])
        self.assertEqual(results, ["John", "Jane"])

    def _createEmptyBoard(self):                    # TODO: Testcases would increaes if custom dimensions are added
        newGame = Connect4()        
        emptyBoard7x6 = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
        self.assertEqual(Connect4._createEmptyBoard, emptyBoard7x6)     # Default game dimensions are 7x6

if __name__ == "__main__":
    unittest.main()
