from random import randint


class Player:
    def __init__(self, player_type, piece):
        self.player_type = player_type
        self.piece = piece
        self.color = "YELLOW" if piece == 1 else "RED"

    def automove(self, options):
        return options[randint(0, len(options) - 1)]

    def is_computer(self):
        return self.player_type != 0
