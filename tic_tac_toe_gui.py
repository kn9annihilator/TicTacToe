import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Initialize variables
current_player = "X"
board = [[" " for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]

# Function to check for a winner
def check_winner():
    global board
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True
    if board[0][0] == board[1][1] == board[2][2] != " " or board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    return False

# Function to check for a draw
def check_draw():
    global board
    return all([cell != " " for row in board for cell in row])

# Function to handle button click
def button_click(row, col):
    global current_player
    if board[row][col] == " ":
        # Update board and button text
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)

        # Check if the current player won
        if check_winner():
            messagebox.showinfo("Tic-Tac-Toe", f"Player {current_player} wins!")
            reset_game()
        elif check_draw():
            messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
            reset_game()
        else:
            # Switch player
            current_player = "O" if current_player == "X" else "X"
    else:
        messagebox.showwarning("Tic-Tac-Toe", "This spot is already taken!")

# Function to reset the game
def reset_game():
    global board, current_player
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text=" ")

# Create the buttons
for row in range(3):
    for col in range(3):
        button = tk.Button(root, text=" ", font=("Arial", 20), height=3, width=6,
                           command=lambda row=row, col=col: button_click(row, col))
        button.grid(row=row, column=col)
        buttons[row][col] = button

# Start the GUI event loop
root.mainloop()
