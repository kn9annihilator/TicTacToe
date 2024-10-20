# Tic-Tac-Toe Game (Console Version)

# Step 1: Create the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Step 2: Get player input and mark the board
def player_move(board, player):
    while True:
        move = input(f"Player {player}, enter your move (row and column): ").split()
        row, col = int(move[0]), int(move[1])
        if board[row][col] == " ":
            board[row][col] = player
            break
        else:
            print("This spot is already taken! Try again.")

# Step 3: Check for winner
def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if all([spot == player for spot in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

# Step 4: Check for draw
def check_draw(board):
    return all([spot != " " for row in board for spot in row])

# Main function to run the game
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]  # 3x3 board
    current_player = "X"

    while True:
        print_board(board)
        player_move(board, current_player)

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Start the game
if __name__ == "__main__":
    tic_tac_toe()
