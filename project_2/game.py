import os
import time
import random

# --- Global Variables ---
board = [" " for _ in range(9)]
current_player = "X"
game_running = True
scores = {"X": 0, "O": 0, "Tie": 0}

# --- Visuals & Colors ---
class Color:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    print(Color.HEADER + Color.BOLD + "==============================" + Color.END)
    print(Color.HEADER + Color.BOLD + "   ULTIMATE TIC TAC TOE       " + Color.END)
    print(Color.HEADER + Color.BOLD + "==============================" + Color.END)

def print_scoreboard():
    print(f"\n{Color.YELLOW}SCOREBOARD:{Color.END} X: {scores['X']} | O: {scores['O']} | Ties: {scores['Tie']}\n")

def print_board(board):
    print("     |     |     ")
    print(f"  {colorize(board[0])}  |  {colorize(board[1])}  |  {colorize(board[2])}  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print(f"  {colorize(board[3])}  |  {colorize(board[4])}  |  {colorize(board[5])}  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print(f"  {colorize(board[6])}  |  {colorize(board[7])}  |  {colorize(board[8])}  ")
    print("     |     |     ")

def colorize(char):
    if char == "X":
        return Color.RED + "X" + Color.END
    elif char == "O":
        return Color.BLUE + "O" + Color.END
    return char

# --- Game Logic ---

def check_win(board, player):
    # Winning combinations (Indices)
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # Columns
        (0, 4, 8), (2, 4, 6)             # Diagonals
    ]
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def check_tie(board):
    return " " not in board

def get_computer_move(board):
    # 1. Try to Win
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            if check_win(board, "O"):
                board[i] = " "
                return i
            board[i] = " " # Undo

    # 2. Block Player
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            if check_win(board, "X"):
                board[i] = " "
                return i
            board[i] = " " # Undo
    
    # 3. Take Center
    if board[4] == " ":
        return 4

    # 4. Take Random Move
    available_moves = [i for i, spot in enumerate(board) if spot == " "]
    return random.choice(available_moves)

def play_game(mode):
    global board, current_player
    board = [" " for _ in range(9)] # Reset board
    current_player = "X"
    running = True

    while running:
        clear_screen()
        print_header()
        print_scoreboard()
        print_board(board)
        
        print(f"\nPlayer {Color.BOLD}{current_player}'s{Color.END} turn.")

        # Handle Move
        if mode == "PvC" and current_player == "O":
            print("Computer is thinking...")
            time.sleep(0.8)
            move = get_computer_move(board)
        else:
            try:
                move = int(input("Enter position (1-9): ")) - 1
            except ValueError:
                continue

        if 0 <= move <= 8 and board[move] == " ":
            board[move] = current_player
            
            # Check Win/Tie
            if check_win(board, current_player):
                clear_screen()
                print_header()
                print_board(board)
                print(f"\n{Color.GREEN}CONGRATULATIONS! Player {current_player} WINS!{Color.END}")
                scores[current_player] += 1
                running = False
            elif check_tie(board):
                clear_screen()
                print_header()
                print_board(board)
                print(f"\n{Color.YELLOW}IT'S A TIE!{Color.END}")
                scores["Tie"] += 1
                running = False
            else:
                # Switch Player
                current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid move! Try again.")
            time.sleep(1)
    
    input("\nPress Enter to return to menu...")

# --- Menu System ---

def main_menu():
    while True:
        clear_screen()
        print_header()
        print("1. Player vs Player (Multiplayer)")
        print("2. Player vs Computer (AI Mode)")
        print("3. Reset Score")
        print("4. Exit")
        print("==============================")
        
        choice = input("Select an option (1-4): ")
        
        if choice == '1':
            play_game("PvP")
        elif choice == '2':
            play_game("PvC")
        elif choice == '3':
            scores["X"] = 0
            scores["O"] = 0
            scores["Tie"] = 0
            print("Scores reset!")
            time.sleep(1)
        elif choice == '4':
            print("Thanks for playing!")
            break
        else:
            print("Invalid selection.")
            time.sleep(1)

if __name__ == "__main__":
    main_menu()