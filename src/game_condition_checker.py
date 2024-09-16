class GameCondition:
    def __init__(self, board, empty):
        self.board = board
        self.empty = empty
        self.WIN_COMBINATIONS = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]

    def check_draw(self):
        return self.empty not in self.board

    def check_win(self):
        for combo in self.WIN_COMBINATIONS:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return self.board[combo[0]]
        return None

    def main(self):
        while not self.check_win() or self.check_draw():
            continue
