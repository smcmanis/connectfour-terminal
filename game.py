class Game:
    def __init__(self, board, players):
        self.board = board
        self.players = players
        self.last_move = None

    def is_over(self):
        return self.board.is_connect_four(move) or self.board.is_full()

    def last_move_is_connect_four(self):
        if self.last_move is None:
            return False

        return self.board.is_connect_four()
