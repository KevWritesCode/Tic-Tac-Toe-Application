# Tic-Tac-Toe-Application
The Tic-Tac-Toe Application is a Python-based game that allows users to play against either a computer or another player. 

Description:
The Tic-Tac-Toe Application is a two-player or one-player game built using the Python programming language. This application allows the user to play against either a computer or another player. The game is played on a 3x3 grid, and the objective is to place three of your symbols (X or O) in a row, either vertically, horizontally, or diagonally. The first player to achieve this wins the game.

Key Parts of the Code:

- The code starts by creating a 3x3 board as a list of lists, with all the elements initially set to ' '.
- The game allows the player to select either 1 player or 2 players mode. If the player selects 1 player, they will play against the computer. If the player selects 2 players, they will play against another player.
- The code then enters into a while loop, where it continues to play until either a player wins or all the spaces on the board are filled (a draw).
- In each iteration of the loop, the code first prints the current board state and then asks the player (or computer) to make a move. The move is made by updating the board list with the player's symbol (X or O).
- The code then checks if the game is over (either a win or a draw) by using the 'is_victory' and 'is_draw' functions. If the game is over, the code breaks out of the loop and prints the outcome.

Design Decisions:

- The game was implemented using a while loop and if-elif statements. This allowed us to keep playing the game until either a player wins or the game ends in a draw.
- The 'is_victory' function was used to check if a player has won the game by checking if they have placed three symbols in a row, either vertically, horizontally, or diagonally.
- The 'is_draw' function was used to check if all the spaces on the board are filled, meaning the game has ended in a draw.
- The code was tested by playing several games, both with one player and two players, to ensure it was functioning correctly.

Reflection:
- Working on this project was a great opportunity to practice using lists, loops, and control statements in Python. I faced challenges in writing the 'is_victory' function, but I was able to overcome it by breaking down the problem into smaller parts and using nested for loops.

Additional Resources:

- Python documentation was used as a reference for syntax and function definitions: https://docs.python.org/3/library/index.html
