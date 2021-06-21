HUMAN = 0
COMPUTER_EASY = 1

def prompt_select_player(player=""):
    options = [
        ":: 0: Human",
        ":: 1: Computer (easy)"
    ]
    print('\n'.join(options))
    choice = input(f"==> Select player {player} type (default: 0): ")
    if choice == 0:
        print(f"Player {player} is Human")
        return HUMAN
    else:
        print(f"Player {player} is Computer (easy)")
        return COMPUTER_EASY

def main():
    try:
        playerRed = prompt_select_player("RED")
        playerYellow = prompt_select_player("YELLOW")
    except KeyboardInterrupt:
        sys.exit()

if __name__ == "__main__":
    main()
        

