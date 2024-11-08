'''
Unit Tests for connect4.py
Jireh Chen, 6th Nov 2024
'''

from connect4 import *
from gameController import *
from gameBoard import *

import unittest
from unittest.mock import patch, Mock

class UnitTesting(unittest.TestCase):

    @patch('builtins.input')
    def test_namePlayers(self, mocked_input):
        game = Connect4()
        mocked_input.side_effect = ["John", "Jane"]
        game._namePlayers()
        self.assertEqual(game._playerNames, {1: 'John', 2: 'Jane'})

    def _createEmptyBoard(self):                    # TODO: Testcases would increaes if custom dimensions are added
        emptyBoard7x6 = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
        self.assertEqual(Connect4._createEmptyBoard, emptyBoard7x6)     # Default game dimensions are 7x6

class GameColumnTesting(unittest.TestCase):

    def test_isFullOnInit(self):
        gameColumn = GameColumn(5)
        self.assertEqual(gameColumn.isFull(), False)



if __name__ == "__main__":
    unittest.main()
