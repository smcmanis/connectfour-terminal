DEFAULT_HEIGHT = 6
DEFAULT_WIDTH = 7
PIECE_RED = 0
PIECE_YELLOW = 1
PIECE_NONE = -1


class Board:
    def __init__(self, height: int = DEFAULT_HEIGHT, width: int = DEFAULT_WIDTH):
        self.columns = [[PIECE_NONE for y in range(height)] for x in range(width)]
        self.height = height
        self.width = width
        self.last_drop = None

    def pieces_in_column(self, x):
        return self.height - self.columns[x].count(PIECE_NONE)

    def pieces_in_board(self):
        return sum(self.pieces_in_column(x) for x in range(self.width))

    def drop_piece(self, x, piece: int = 0):
        y = self.pieces_in_column(x)
        self.columns[x][y] = piece
        self.last_drop = (x, y)

    def get_row(self, y):
        return [self.columns[x][y] for x in range(self.width)]

    def get_valid_moves(self):
        return [x for x in range(self.width) if self.pieces_in_column(x) != self.height]

    def is_out_of_bounds(self, x, y):
        return x < 0 or x >= self.width or y < 0 or y >= self.height

    def is_full(self):
        for x in range(self.width):
            if self.pieces_in_column(x) < self.height:
                return False
        return True

    def last_drop_makes_connectfour(self):
        if self.last_drop is None:
            return False

        x, y = self.last_drop
        piece = self.columns[x][y]

        # Look for vertical connected four (3 spots below)
        if y - 3 >= 0 and self.columns[x][y - 3 : y].count(piece) == 3:
            return True

        # Look for horizontal (xxx[x] to [x]xxx)
        for dx in range(4):
            if self.is_out_of_bounds(x - dx, y) or self.is_out_of_bounds(x - dx + 4, y):
                continue
            cols = self.columns[x - dx : x - dx + 4]
            count = [col[y] for col in cols].count(piece)
            if count == 4:
                return True

        # Look for diagonal
        for dx in range(3):
            for gradient in [-1, 1]:
                if self.is_out_of_bounds(
                    x - dx, y - gradient * (dx)
                ) or self.is_out_of_bounds(x - dx + 4, y - gradient * (dx + 4)):
                    continue

                diagonal = [
                    self.columns[x - dx + i][y - gradient * (dx + i)] for i in range(3)
                ]
                if diagonal.count(piece) == 4:
                    return True

        return False
