"""
Tic Tac Toe Player
"""

import math,copy

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
    x,o = 0,0
    for i in range(3) : 
        x += board[i].count(X)
        o += board[i].count(O)
    if x == o: return X 
    return O
    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    ans = list()
    for x in range(3) : 
        for y in range(3) : 
            if (board[x][y] == EMPTY) : ans.append((x,y))
    return ans

    # raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # action = list(action)
    p = player(board)
    # print(action[0])
    newboard = copy.deepcopy(board)
    # print(action[0],action[1])d
    newboard[action[0]][action[1]] = p
    return newboard
    # raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3) : 
        if board[i] == [X]*3 : return X
        if board[i] == [O]*3 : return O 
        if board[0][i] == board[1][i] == board[2][i] == X : return X 
        if board[0][i] == board[1][i] == board[2][i] == O : return O
    if board[0][0] == board[1][1] == board[2][2]  : return  board[0][0]
    if board[0][2] == board[1][1] == board[2][0] : return board[1][1]
    return None 
        
    # raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None : return True 
    ans = 0
    for i in range(3) : 
        ans += board[i].count(EMPTY)
    return True if ans == 0 else False 
    # raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    ans = winner(board)
    if ans is None : return 0 
    return 1 if ans == 1 else -1 
    # raise NotImplementedError

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    Max = float("-inf")
    Min = float("inf")

    if player(board) == X:
        return Max_Value(board,Max,Min)[1]
    else:
        return Min_Value(board,Max,Min)[1]

def Max_Value(board,Max,Min):
    move = None
    if terminal(board):
        return [utility(board), None];
    v = float('-inf')
    for action in actions(board):
        test = Min_Value(result(board, action),Max,Min)[0]
        Max = max(Max, test)
        if test > v:
            v = test
            move = action
        if Max >= Min:
            break
    return [v, move];

def Min_Value(board,Max,Min):
    move = None
    if terminal(board):
        return [utility(board), None];
    v = float('inf')
    for action in actions(board):
        test = Max_Value(result(board, action),Max,Min)[0]
        Min = min(Min, test)
        if test < v:
            v = test
            move = action
        if Max >= Min:
            break
    return [v, move];
    # raise NotImplementedError
    
