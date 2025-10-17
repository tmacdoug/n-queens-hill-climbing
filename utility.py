import random


#Validate the board state
#1: Valid end state
#0: Valid state
#-1: Invalid state
def calculate_h(board):
    n = len(board)
    valid = True
    attacking = 0

    #Check each row
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 1:
                #Check rows
                for check_row in range(col+1, len(board)):
                    if board[row][check_row] == 1: attacking += 1
                #Check columns
                for check_col in range(row+1, len(board)):
                    if board[check_col][col] == 1: attacking += 1
                #Check diagonals
                #Up-left
                diag = 1
                while min(row, col) - diag >= 0:
                    if board[row-diag][col-diag] == 1: attacking += 1
                    diag += 1
                #Up-right
                diag = 1
                while row+diag < n and col-diag >= 0:
                    if board[row+diag][col-diag] == 1: attacking += 1
                    diag += 1
                #Down-left
                diag = 1
                while row-diag >=0 and col+diag < n:
                    if board[row-diag][col+diag] == 1: attacking += 1
                    diag += 1
                #Down-right
                diag = 1
                while diag + max(row, col) < len(board):
                    if board[row+diag][col+diag] == 1: attacking += 1
                    diag += 1

    
    return attacking


#Helper function to print board in a user-friendly manner
def print_board(board):
    to_print = ""
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0: to_print += "-"
            else: to_print += "Q"
        to_print += "\n"
    print(to_print)


def initialize_board(n):
    board = [ [0]*n for i in range(n)]

    for i in range(n):
        row = random.randint(0,n-1)
        board[row][i] = 1
    return board