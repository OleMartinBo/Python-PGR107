
# Tic Tac Toe game in Python

board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
player = 1

def display_board():
    print("Player 1: X")
    print("Player 2: O")
    print(board[1],'|',board[2],'|',board[3])
    print("---------")
    print(board[4],'|',board[5],'|',board[6])
    print("---------")
    print(board[7],'|',board[8],'|',board[9])

def check_win():
    if (board[1] == board[2] and board[2] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[5] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[8] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[4] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[5] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[6] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[5] == board[9] and board[1] != ' '):
        return True
    elif (board[3] == board[5] and board[5] == board[7] and board[3] != ' '):
        return True
    else:
        return False

while True:
    display_board()
    if player == 1:
        print("Player 1's turn")
    else:
        print("Player 2's turn")

    try:
        choice = int(input("Enter the position where you want to mark (1-9): "))
    except ValueError:
        print("Wrong input. Please enter a number between 1 and 9.")
        continue

    if board[choice] == ' ':
        if player == 1:
            board[choice] = 'X'
            player = 2
        else:
            board[choice] = 'O'
            player = 1
    else:
        print("The place is already filled.\nChoose another place...")
        continue

    if check_win():
        display_board()
        if player == 1:
            print("Player 2 wins!")
        else:
            print("Player 1 wins!")
        break
    elif ' ' not in board:
        print("It's a tie!")
        break
