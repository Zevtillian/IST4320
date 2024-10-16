import sys

def clear_screen():
    # A simple function to clear the console screen.
    print("\033c", end="")

class TicTacToe:
    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]
        self.current_player = "X"

    def print_board(self):
        clear_screen()
        print("\n" + " | ".join(self.board[:3]))
        print("-" * 9)
        print(" | ".join(self.board[3:6]))
        print("-" * 9)
        print(" | ".join(self.board[6:9]) + "\n")

    def make_move(self, position):
        if self.board[position - 1] != "X" and self.board[position - 1] != "O":
            self.board[position - 1] = self.current_player
            return True
        else:
            return False

    def switch_player(self):
        self.current_player = "X" if self.current_player == "O" else "O"

    def check_winner(self):
        for combo in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]]:
                return True
        return False

    def is_board_full(self):
        return all(cell == "X" or cell == "O" for cell in self.board)

def play_game():
    game = TicTacToe()
    while True:
        game.print_board()
        position = int(input(f"Player {game.current_player}, enter a position (1-9): "))
        
        if position < 1 or position > 9:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue
        
        if game.make_move(position):
            if game.check_winner():
                game.print_board()
                print(f"Player {game.current_player} wins!")
                break
            elif game.is_board_full():
                game.print_board()
                print("It's a draw!")
                break
            game.switch_player()
        else:
            print("That position is already taken. Try again.")

if __name__ == "__main__":
    play_game()
    sys.exit()
