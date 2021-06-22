class bcolors:
    YELLOW = "\033[93m"
    RED = "\033[31m"
    BLACK = "\033[0m"


TOKENS = {-1: " ", 0: "R", 1: "Y"}
TOKEN_COLORS = {-1: bcolors.BLACK, 0: bcolors.RED, 1: bcolors.YELLOW}


def color_text(text, color):
    return f"{color}{text}{bcolors.BLACK}"


def draw_row(row):
    colored_tokens = [color_text(TOKENS[token], TOKEN_COLORS[token]) for token in row]
    return "|" + "|".join(colored_tokens) + "|"


def draw_board(board):
    rows = []
    for y in range(board.height - 1, -1, -1):
        row = board.get_row(y)
        rows.append(draw_row(row))

    print("\n".join(rows))
