class GameLogic:
    def __init__(self):
        self.empty = " "
        self.board = [self.empty] * 9
        self.p1 = "X"
        self.p2 = "O"
        self.current_player = self.p1

    def play_turn(self, cell):
        if self.board[cell] == self.empty:
            self.board[cell] = self.current_player
            self.current_player = self.p2 if self.current_player == self.p1 else self.p1
