import unittest
from challenge3 import Board, check_for_win

class TestTicTacToe(unittest.TestCase):
    def test_check_for_win(self):
        #arrange: set up board for test case
        board = Board()
        board.board = [
            ['x','x','x']
            [' ',' ',' ']
            [' ',' ',' ']
        ]
        # Act: call the function being tested
        result = check_for_win()

        # assert: check that it works
        self.assertTrue(result, "should detect a winning row")

if __name__ == '__main__':
    unittest.main()