import copy
import sys

def get_winner(board):
    types = ["X", "O"]

    for type in types:
        # Check rows
        for row in board:
            if all(cell == type for cell in row):
                return type

        # Check columns
        for col in range(3):
            if all(board[row][col] == type for row in range(3)):
                return type

        # Check diagonals
        if all(board[i][i] == type for i in range(3)):
            return type
        if all(board[i][2 - i] == type for i in range(3)):
            return type

    # If there's any empty cell, no winner yet
    if any(cell == " " for row in board for cell in row):
        return None  # Game still going

    return "tie"

def getAImove(board, turn, top_level, iiiiii):
    winner = get_winner(board)
    new_board = copy.deepcopy(board)
    if iiiiii == 0:
        return([0, 0])
    if winner != None:
        if winner == "X":
            return -1
        elif winner == "O":
            return 1
        elif winner == "tie":
            return 0
    if turn == "O":
        best_score = float('-inf')
        best_move = [0, 0]
        for row in range(3):
            for col in range(3):
                score = 0
                new_board = copy.deepcopy(board)
                if board[row][col] == " ":
                    new_board[row][col] = turn
                    score = getAImove(new_board, "X", False, 8)
                    if score > best_score:
                        best_score = score
                        best_move = [row, col]
    elif turn == "X":
        best_score = float('inf')
        best_move = [0, 0]
        for row in range(3):
            for col in range(3):
                score = 0
                new_board = copy.deepcopy(board)
                if board[row][col] == " ":
                    new_board[row][col] = turn
                    score = getAImove(new_board, "O", False, 8)
                    if score < best_score:
                        best_score = score
                        best_move = [row, col]
    if top_level:
        return(best_move)
    else:
        return(best_score)
       
def get_input(prompt, expected_type):
    print(prompt)
    # Mapping from Python types to friendly descriptions
    friendly_names = {
        int: "whole number",
        float: "decimal number",
        str: "text",
        bool: "true/false value"
    }

    while True:
        try:
            # Get input from user and try to convert to the expected type
            value = input("> ")
            if value.lower() in ["admin quit", "adm quit", "adm qt", "admin qt", "adminquit", "admquit", "admqt", "adminqt"]:
                sys.exit()

            # Special case for bool
            if expected_type is bool:
                if value.lower() in ["true", "t", "yes", "y", "1"]:
                    return True
                elif value.lower() in ["false", "f", "no", "n", "0"]:
                    return False
                else:
                    raise ValueError("Not a valid boolean.")

            return expected_type(value)

        except ValueError:
            print(f"Please enter a valid {friendly_names.get(expected_type, 'value')}.")

def printBoard(board):
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]}")
    print("-----------")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]}")
    print("-----------")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]}")

def runRound():
    winner = None
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
        ]
    turn_names = {0: "your", 1: "the computer's"}
    if get_input("Do you want to go first? (Tip: You should, to try and get a draw)", bool):
        turn = 0
    else:
        turn = 1

    iiiiiii = 0

    while winner == None:
        printBoard(board)
        if turn == 0:
            while True:
                player_x = get_input("Which row do you want to move in? (1, 2, 3)", int) - 1
                player_y = get_input(f"Which column of row {player_x + 1} do you want to move in? (1, 2, 3)", int) - 1
                if player_x not in range(3) or player_y not in range(3):
                    print("Invalid move - out of bounds")
                elif board[player_x][player_y] != " ":
                    print("Invalid move - space already taken")
                else:
                    break
            board[player_x][player_y] = "X"
            print(f"You moved in row {player_x + 1}, column {player_y + 1}")
        elif turn == 1:
            print("The AI is thinking...")
            ai_x, ai_y = getAImove(board, "O", True, iiiiiii)
            print(f"The AI moved in row {ai_x + 1}, column {ai_y + 1}")
            board[ai_x][ai_y] = "O"
        turn = (turn + 1) % 2
        iiiiiii += 1
        winner = get_winner(board)
    if winner == "tie":
        print("It's a tie!")
    elif winner == "X":
        print('"X" (Player) wins!')
    elif winner == "O":
        print('"O" (AI) wins!')
    printBoard(board)
runRound()

