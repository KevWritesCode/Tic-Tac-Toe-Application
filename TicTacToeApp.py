# Tic Tac Toe Game in Python

board = [' ' for x in range(9)]

def print_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)

def player_move(icon):
    if icon == 'X':
        player = 1
    elif icon == 'O':
        player = 2

    print("Your turn player {}".format(player))
    choice = int(input("Enter your move (1-9): ").strip())
    if board[choice - 1] == ' ':
        board[choice - 1] = icon
    else:
        print()
        print("That space is already taken!")

def is_victory(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
       (board[3] == icon and board[4] == icon and board[5] == icon) or \
       (board[6] == icon and board[7] == icon and board[8] == icon) or \
       (board[0] == icon and board[3] == icon and board[6] == icon) or \
       (board[1] == icon and board[4] == icon and board[7] == icon) or \
       (board[2] == icon and board[5] == icon and board[8] == icon) or \
       (board[0] == icon and board[4] == icon and board[8] == icon) or \
       (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False

def is_draw():
    if ' ' not in board:
        return True
    else:
        return False

def computer_move(icon):
    import random
    while True:
        move = random.randint(0,8)
        if board[move] == ' ':
            board[move] = icon
            break

def main():
    print("Tic Tac Toe")
    print("Instructions:")
    print("1. The game is played on a 3x3 grid.")
    print("2. Player 1 will use the 'X' icon and player 2 will use the 'O' icon.")
    print("3. Players take turns marking spaces on the grid.")
    print("4. The player who successfully places three of their icons in a row, column, or diagonal wins the game.")
    print("5. If all spaces on the grid are filled and no player has won, the game is a draw.")
    print()

    num_players = int(input("Enter 1 to play against the computer or 2 to play with another player: ").strip())
    while num_players != 1 and num_players != 2:
        print("Invalid input. Please enter either 1 or 2.")
        num_players = int(input("Enter 1 to play against the computer or 2 to play with another player: ").strip())

def main():
    while True:
        num_players = int(input("Enter 1 to play against the computer or 2 to play with another player: ").strip())
        while num_players != 1 and num_players != 2:
            print("Invalid input. Please enter either 1 or 2.")
            num_players = int(input("Enter 1 to play against the computer or 2 to play with another player: ").strip())

        if num_players == 1:
            game_over = False
            while not game_over:
                print_board()
                player_move('X')
                print_board()
                if is_victory('X'):
                    print("X wins! Congratulations!")
                    game_over = True
                elif is_draw():
                    print("It's a draw!")
                    game_over = True
                else:
                    computer_move('O')
                    print_board()
                    if is_victory('O'):
                        print("O wins! Better luck next time.")
                        game_over = True
                    elif is_draw():
                        print("It's a draw!")
                        game_over = True
        else:
            game_over = False
            while not game_over:
                print_board()
                player_move('X')
                print_board()
                if is_victory('X'):
                    print("X wins! Congratulations!")
                    game_over = True
                elif is_draw():
                    print("It's a draw!")
                    game_over = True
                else:
                    player_move('O')
                    print_board()
                    if is_victory('O'):
                        print("O wins! Congratulations!")
                        game_over = True
                    elif is_draw():
                        print("It's a draw!")
                        game_over = True

main()
