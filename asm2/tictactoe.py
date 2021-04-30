"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count = 0
    for row in board:
        for cell in row:
            if cell is EMPTY:
                count += 1

    if count % 2 == 0:
        return 'O'
    return 'X'

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    output = list()
    # if board is None:
    #     for i in range(3):
    #         for j in range(3):
    #             output.append(tuple([i, j]))
    #     return output
    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                output.append(tuple([i, j]))
    return output


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    returning_board = copy.deepcopy(board)
    if board[action[0]][action[1]] is EMPTY:
        returning_board[action[0]][action[1]] = player(returning_board)
        return returning_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check all rows
    for i in range(3):
        if board[i][0] == 'X' and board[i][1] == 'X' and board[i][2] == 'X':
            return 'X'
        if board[i][0] == 'O' and board[i][1] == 'O' and board[i][2] == 'O':
            return 'O'
    
    # Check all columns
    for i in range(3):
        if board[0][i] == 'X' and board[1][i] == 'X' and board[2][i] == 'X':
            return 'X'
        if board[0][i] == 'O' and board[1][i] == 'O' and board[2][i] == 'O':
            return 'O'

    # Check diagonal
    if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
        return 'X'
    if board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
        return 'O'
    if board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
        return 'X'
    if board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
        return 'O'

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == 'X':
        return 1
    if winner(board) == 'O':
        return -1
    return 0

def max_value(board):
    if terminal(board):
        return utility(board)
    v = -10
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = 10
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board) is True:
        return None
    actions_list = actions(board)
    values = list()
    if player(board) is 'X':    
        for action in actions_list:
            values.append(min_value(result(board, action)))
        max_index = values.index(max(values))
        return actions_list[max_index]
    else:
        for action in actions_list:
            values.append(max_value(result(board, action)))
        min_index = values.index(min(values))
        return actions_list[min_index]
