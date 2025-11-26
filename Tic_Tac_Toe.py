import random

def display_board(board):
    for row in board:
        print(row)
    print()

def check_winner(board, symbol):
    # Rows
    for r in range(3):
        if board[r][0] == board[r][1] == board[r][2] == symbol:
            return True

    # Columns
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] == symbol:
            return True

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        return True
    if board[0][2] == board[1][1] == board[2][0] == symbol:
        return True

    return False

def board_full(board):
    for row in board:
        if "_" in row:
            return False
    return True

def random_system_move(board):
    empty = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == "_":
                empty.append((i, j))

    return random.choice(empty)

# Main game
board = [["_", "_", "_"],
         ["_", "_", "_"],
         ["_", "_", "_"]]

player = "X"
system = "O"
current = player

while True:
    display_board(board)

    if current == player:
        print("Your move (row col): ")
        r, c = map(int, input().split())
        r -= 1; c -= 1

        if board[r][c] != "_":
            print("Invalid move! Try again.")
            continue
        board[r][c] = player

    else:
        print("System is thinking...")
        r, c = random_system_move(board)
        board[r][c] = system
        print("System moved:", r+1, c+1)

    if check_winner(board, current):
        display_board(board)
        print("Winner:", "You!" if current == player else "System")
        break

    if board_full(board):
        display_board(board)
        print("Game Draw!")
        break

    current = system if current == player else player
