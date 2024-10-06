import unittest
from game_logic import GameLogic


class TestGameLogic(unittest.TestCase):
    def test_play_turn(self):
        game = GameLogic()
        game.play_turn(0)  # Player 1 ('X') plays turn at cell 0
        self.assertEqual(game.board[0], 'X')
        self.assertEqual(game.current_player, 'O')  # Next player should be 'O'

        game.play_turn(1)  # Player 2 ('O') plays turn at cell 1
        self.assertEqual(game.board[1], 'O')
        self.assertEqual(game.current_player, 'X')  # Next player should be 'X'

    def test_invalid_move(self):
        game = GameLogic()
        game.play_turn(0)  # Player 1 ('X') plays turn at cell 0
        game.play_turn(0)  # Invalid move (cell 0 is already taken)
        self.assertEqual(game.board[0], 'X')  # Cell 0 should still have 'X'
