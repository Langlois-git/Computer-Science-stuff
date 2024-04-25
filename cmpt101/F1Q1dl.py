
# Integrity pledge: This submission is my own work, except where I have acknowledged the use of the works of other people. 
#-------------------------------------
#  Name:     	David Langlois
#  Program:     F1Q1dl.py	
# ------------------------------------
# Purpose:  The purpose of this program is to classify a user defined food item into 1 of 6 catergories.


def create_board():
    '''
    
This function creates the game board.

:return It returns the game board as a list
    
    '''
    board = ["b", "b", "b", "b", "b", "-", "w", "w", "w", "w", "w"]
    return board


def display_board(board):
    '''
    
This function displays the game board

:param board It accepts the game board as a list 
    
    '''
    for i in board:
        print(i, end = " ")
    print("")
    print("0 1 2 3 4 5 6 7 8 9 10")

def can_move(board, move):
    '''
    
This function determines if the player selected position is a legal move

:param board It accepts the game board as a list 

:param move It accepts a move index as an integer

:return True or False It returns a decision as a boolean
    
    '''
    if board[move] == "b" and board[move+1] == "-":
        return True
    if board[move] == "w" and board[move-1] == "-":
        return True
    else:
        return False

def can_jump(board, move):
    '''
    
This function determines if the player selected position is a legal jump

:param board It accepts the game board as a list 

:param move It accepts a jump index as an integer

:return True or False It returns a decision as a boolean

    '''
    if board[move] == "b" and board[move+2] == "-":
        return True
    if board[move] == "w" and board[move-2] == "-":
        return True
    else:
        return False

def make_move(board, move):
    '''
    
This function applies the player choosen move to the board

:param board It accepts the game board as a list 

:param move It accepts a move index as an integer

:return board It returns the board as a list with the move applied
    
    '''
    if board[move] == 'b':
        tmp = board[move+1]
        board[move+1] = board[move]
        board[move] = tmp
    else:
        tmp = board[move-1]
        board[move-1] = board[move]
        board[move] = tmp
    return board

def make_jump(board, move):
    '''
    
This function applies the player choosen jump to the board

:param board It accepts the game board as a list 

:param move It accepts a jump index as an integer

:return board It returns the board as a list with the jump applied
    
    '''
    if board[move] == 'b':
        tmp = board[move+2]
        board[move+2] = board[move]
        board[move] = tmp
    else:
        tmp = board[move-2]
        board[move-2] = board[move]
        board[move] = tmp
    return board


def move_exists(board):
    '''
    
This function checks to see if any moves exsist

:param board It accepts the game board as a list 

:return True or False as a boolean
    
    '''
    for i in range(0, len(board)):
        if can_move(board, i) or can_jump(board, i):
            return True
    return False


def get_move():
    '''
    
This function accepts player input

:return move as an integer from the player input
    
    '''
    move = int(input("Enter a move 0 to 10: "))
    print("")
    return move


def winner(board):
    '''
    
This function checks to see if the board is in it's winning state

:param board It accepts the game board as a list 

:return True or False as a boolean
    
    '''
    if board == ["w", "w", "w", "w", "w", "-", "b", "b", "b", "b", "b"]:
        return True
    else:
        return False

def marching_pegs():
    '''
    
This function defines the marching_pegs game logic

    '''
    board = create_board()
    while move_exists(board):
        display_board(board)
        move = get_move()
        if can_move(board, move):
            board = make_move(board, move)
        elif can_jump(board, move):
            make_jump(board, move)
        else:
            print("You cannot make that move...")
            print("")
    print("And thats the end of the game folks.")
    display_board(board)
    if winner(board):
        print("You win")

marching_pegs()


