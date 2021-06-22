import sys

from player import Player
from board import Board, PIECE_NONE, PIECE_RED, PIECE_YELLOW
from console import draw_board


class Game:
    def __init__(self, board, players):
        self.players = players
        self.current_player = PIECE_RED
        self.board = board

    def get_move(self, player):
        if player.is_computer():
            move = player.automove(self.board.get_valid_moves())
            self.board.drop_piece(move, self.current_player)
            print(f"Computer dropped in column {move}")
            return
        else:
            while True:
                try:
                    choice = int(
                        input(
                            f"==> Enter column to drop piece {self.board.get_valid_moves()}: "
                        )
                    )
                    if choice in self.board.get_valid_moves():
                        self.board.drop_piece(choice, self.current_player)
                        return
                    else:
                        print("invalid selection! Try again")
                except:
                    print("invalid selection! Try again")

    def start(self):
        while True:

            if self.board.is_full():
                print("Game over: No player wins")
                return

            print()
            draw_board(self.board)
            print()

            if self.board.last_drop_makes_connectfour():
                self.current_player ^= 1
                print(f"{self.players[self.current_player].color} wins!")
                return

            self.get_move(self.players[self.current_player])

            self.current_player ^= 1


def prompt_select_player(player=""):
    options = [":: 0: Human", ":: 1: Computer (easy)"]
    print("\n".join(options))
    choice = input(f"==> Select player {player} type (default: 0): ")
    if choice is "":
        choice = 0

    choice = int(choice)
    if choice == 0:
        print(f"Player {player} is Human")
        return choice
    else:
        print(f"Player {player} is Computer (easy)")
        return choice


def main():
    try:
        while True:
            players = []
            players.append(Player(prompt_select_player("RED"), PIECE_RED))
            players.append(Player(prompt_select_player("YELLOW"), PIECE_YELLOW))
            board = Board()
            Game(board, players).start()
            restart = input("Play again? [y]").lower()
            if restart != "y":
                sys.exit()
    except KeyboardInterrupt:
        sys.exit()


if __name__ == "__main__":
    main()
