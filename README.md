# TicTacToe
Tic-Tac-Toe Console Game
This project is a simple console-based implementation of the classic Tic-Tac-Toe game. It is a two-player game where the players take turns marking their respective symbols ("X" or "O") on a 3x3 grid. The goal is to place three marks in a horizontal, vertical, or diagonal line.

Table of Contents
How to Play
Features
Game Mechanics
How to Run
Project Structure
Future Enhancements
Acknowledgements
How to Play
The game is played between two players (Player X and Player O).
The players take turns entering their moves by specifying the row and column numbers (both starting from 0).
A player wins if they can align three of their symbols in a row, column, or diagonal.
If all spots on the board are filled and no player has won, the game is declared a draw.
Features
Interactive gameplay: Players are prompted to enter their moves, and the game board is updated dynamically.
Win detection: The game checks for a winner after every move.
Draw detection: The game ends in a draw if all spaces are filled without a winner.
Game Mechanics
Board Setup:
The game board is a 3x3 grid initialized with empty spaces (" ").
Players mark their moves using "X" and "O".
Player Input:
Players enter their moves in the form of row and column indices (starting from 0).
The game prevents players from making moves in spots that are already taken and asks them to try again.
Win Conditions:
A player wins if they have three of their symbols in any row, column, or diagonal.
Draw Condition:
If all the spaces on the board are filled and no player has won, the game is declared a draw.
How to Run
Clone the repository or copy the tic_tac_toe.py script to your local machine.

Run the script:

bash
Copy code
python tic_tac_toe.py
Follow the prompts to enter your moves as a player. The input format is two numbers separated by space, where:

The first number represents the row (0-2).
The second number represents the column (0-2).
Example of valid input: 0 1

Enjoy the game! After the game ends, you can restart by running the script again.
Project Structure
bash
Copy code
.
├── tic_tac_toe.py        # Main game script
└── README.md             # This readme file
Future Enhancements
Add a graphical user interface (GUI) for better user experience.
Implement an AI-based single-player mode where the user can play against the computer.
Add support for different board sizes, such as 4x4 or 5x5 grids.
Improve error handling for invalid inputs.
Acknowledgements
This project is a basic implementation of Tic-Tac-Toe for educational purposes. It was built using Python.
