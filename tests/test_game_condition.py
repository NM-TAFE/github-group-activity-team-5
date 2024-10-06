import unittest
from game_condition_checker import GameCondition


class TestGameCondition(unittest.TestCase):
    def test_check_draw(self):
        board = ['X', 'O', 'X', 'X', 'X', 'O', 'O', 'X', 'O']  # No empty spaces, no winner
        game = GameCondition(board, ' ')
        self.assertTrue(game.check_draw())  # True if it's a draw

    def test_no_draw(self):
        board = ['X', 'O', 'X', 'X', ' ', 'O', 'O', 'X', 'O']  # Empty space, no draw yet
        game = GameCondition(board, ' ')
        self.assertFalse(game.check_draw())  # False if it's not a draw
