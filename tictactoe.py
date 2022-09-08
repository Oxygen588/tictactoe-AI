"""
Tic Tac Toe Player
"""

from asyncio.windows_events import NULL
import math
from queue import Empty
from telnetlib import theNULL
from turtle import end_fill
winmoves =[[[True, False, False],
            [False, True, False],
            [False, False, True]],
            #-------------------
            [[False, False, True],
            [False, True, False],
            [True, False, False]],
            #-------------------
            [[False, False, False],
            [False, False, False],
            [False, False, False]],
            #-------------------
            [[False, False, False],
            [False, False, False],
            [False, False, False]],
            ]
aaa = [2,1,0]
def verifyboard(board):
    global X
    global O
    k1 = -1
    for k in board:
        k1= k1+1
        Os = 0
        Xs = 0
        for kk in board[k1]:
            if kk == O:
                Os = Os+1
                if Os == 3:
                    print("2")
                    return O
            if kk == X:
                Xs = Xs+1
                if Xs == 3:
                    print("1")
                    return X
    Os = 0
    Xs = 0
    for i in range(0,3):
        Os = 0
        Xs = 0
        for k in board:
            if k[i] == O:
                Os = Os+1
                if Os == 3:
                    print("3")
                    return O
            if k[i] == X:
                Xs = Xs+1
                if Xs == 3:
                    print("4")
                    return X
    Os = 0
    Xs = 0
    for i in range(0,3):
            if board[i][i] == O:
                Os = Os+1
                if Os == 3:
                    print("5")
                    return O
            if board[i][i] == X:
                Xs = Xs+1
                if Xs == 3:
                    print("6")
                    return X
        
    Os = 0
    Xs = 0

    minuss = 3
    for iii in range(0,3):
        minuss = minuss -1
        if board[iii][minuss] == O:
            Os = Os+1
            if Os == 3:
                print("7")
                return O
        if board[iii][minuss] == X:
            Xs = Xs+1
            if Xs == 3:
                print("8")
                return X

    Os = 0
    Xs = 0
    return None
            
def winXmove(board,wh):
 
    k1 = -1
    k2 = -1
    found = False
    global X
    nb = board
    for k in nb:
        k1 = k1 + 1
        if found == False:
            for kk in nb[k1]:
                k2 = k2 + 1
                # print(board[k1][k2])
                if nb[k1][k2] == None and found == False:
                    nb[k1][k2] = wh
                    #print(nb,"Nb",verifyboard(nb))
                    if verifyboard(nb):
                        found = True
                        print("Found")
                        nb[k1][k2] = None
                        return [k1,k2]

                        #   print(board[k1][k2])
                    nb[k1][k2] = None
                        
            k2 = -1
    k2 = -1
    
    return False

X = "X"
O = "O"
EMPTY = None
gameover = False
currentx = False
def currentturn():
    global currentx
    if currentx ==  True:
        currentx = False
        return X
    else:
        currentx = True
        return O
def getturn():
    global currentx
    if currentx ==  True:
        return X
    else:
        return O
def getturn1():
    global currentx
    if currentx ==  True:
        return O
    else:
        return X
def initial_state():
    global moves
    moves = 0
    global gameover
    gameover = False
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
    global currentx
    #print(currentx)

    return getturn()


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    raise NotImplementedError

def is_integer(n):
    try:
 
        if isinstance(n, str):
            return False
        elif type(n) is dict:
            return True
        else:
            print("N",n)
            float(n)
    except ValueError:
        return False
    else:
        return True
moves = 0
isX = None
def result(board, action):
    global moves
    global isX
    moves = moves + 1
    #print(moves)
    global gameover
    """
    Returns the board that results from making move (i, j) on the board.
    """
    found = False
    #print(board[0])

    isX = getturn()
    board[action[0]][action[1]] = getturn()
    found = True
    currentturn()
    if moves == 9 or verifyboard(board):
        gameover = True

    return board


def winner(board):

    #print(verifyboard(board))
    return verifyboard(board)

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
   # print("gameover")
    return gameover


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if verifyboard(board) == "X":
        return 1
    elif verifyboard(board) == "Y":
        return -1
    else:
        return 0

def getplusminus(what):
    if getturn() == what:
        return 1
    elif getturn() != what:
        return -1
    else:
        return 0
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    print("startedminimax")
    possiblilities = {}
    k1 = -1
    k2 = -1
    done = []
    win = False
    wm = winXmove(board,getturn())
    if wm:
        return [wm[0],wm[1]]
    wm = winXmove(board,getturn1())
    if wm:
        return [wm[0],wm[1]]
    for k in board:
        k1 = k1 + 1
        for kk in board[k1]:
            k2 = k2 + 1
            print("ckecked: ",k1,"  ",k2)
            if board[k1][k2] == None:
                board[k1][k2] = getturn1()
                if ([k1,k2] in done) == False:
                    done.append([k1,k2])
                    possiblilities[k1,k2] = {}
                    possiblilities[k1,k2]['result'] = NULL
                k22 = -1
                k11 = -1
              
                if verifyboard(board):
                   
                    if possiblilities[k1,k2]['result'] == NULL:
                        possiblilities[k1,k2]['result'] = 0
                    possiblilities[k1,k2]['result'] = getplusminus(getturn1())+(possiblilities[k1,k2]['result'])
                    possiblilities[k1,k2][k1,k1] = [k1,k2]
                for k in board:
                    k11 = k11 + 1
                    
                    if verifyboard(board):
                   
                        if possiblilities[k1,k2]['result'] == NULL:
                                    possiblilities[k1,k2]['result'] = 0
                        possiblilities[k1,k2]['result'] = getplusminus(getturn1())+(possiblilities[k1,k2]['result'])
                        possiblilities[k1,k2][k1,k1] = [k1,k2]
                    for kk in board[k1]:
                        k22 = k22 + 1
                        if board[k11][k22] == None:
                            board[k11][k22] = getturn1()
                            if verifyboard(board):
                                
                                if possiblilities[k1,k2]['result'] == NULL:
                                    possiblilities[k1,k2]['result'] = 0
                                possiblilities[k1,k2]['result'] = getplusminus(getturn1())+possiblilities[k1,k2]['result']
                                possiblilities[k1,k2][k11,k22] = [k11,k22]
                            board[k11][k22] = None
                    k22 = -1
                k11 = -1

                board[k1][k2] = getturn()
                if ([k1,k2] in done) == False:
                    done.append([k1,k2])
                    possiblilities[k1,k2] = {}
                    possiblilities[k1,k2]['result'] = NULL
                k22 = -1
                k11 = -1
               
                if verifyboard(board):
                 
                    if possiblilities[k1,k2]['result'] == NULL:
                        possiblilities[k1,k2]['result'] = 0
                    possiblilities[k1,k2]['result'] = getplusminus(getturn())+(possiblilities[k1,k2]['result'])
                    possiblilities[k1,k2][k1,k1] = [k1,k2]
                for k in board:
                    k11 = k11 + 1
                    for kk in board[k1]:
                        k22 = k22 + 1
                        if board[k11][k22] == None:
                            board[k11][k22] = getturn()
                            if verifyboard(board):
                           
                                if possiblilities[k1,k2]['result'] == NULL:
                                    possiblilities[k1,k2]['result'] = 0
                                possiblilities[k1,k2]['result'] = getplusminus(getturn())+possiblilities[k1,k2]['result']
                                possiblilities[k1,k2][k11,k22] = [k11,k22]
                            board[k11][k22] = None
                    k22 = -1
                k11 = -1
                board[k1][k2] = None
        k2 = -1
    k2 = -1
    result = -2
    kk = [0,0]
    print(possiblilities)
    for k in possiblilities:
      
        if possiblilities[k[0],k[1]]['result'] != NULL:
            if result<possiblilities[k[0],k[1]]['result']:
                result = possiblilities[k[0],k[1]]['result']
                kk = k
            if result < possiblilities[k[0],k[1]]['result']:
                if possiblilities[k[0],k[1]]['result'] == -1:
                    return k
                if possiblilities[k[0],k[1]]['result'] == 0:
                    return k
    
        if kk == [0,0]:
            k1 = -1
            k2 = -1
            for k in board:
                k1 = k1 + 1
                for kk in board[k1]:
                    k2 = k2 + 1
                    if (k1 == 0 or k1 == 2) and (k2 ==0 or k2 == 2):
                        if board[nott(k1)][nott(k2)] == None:
                            return [nott(k1),nott(k2)]
                k2 = -1
        if kk == [0,0]:
            k1 = -1
            k2 = -1
            for k in board:
                k1 = k1 + 1
                for kk in board[k1]:
                    k2 = k2 + 1
                    if (k1 == 0 or k1 == 2) and (k2 ==0 or k2 == 2):
                        if board[k1][k2] == None:
                            return [k1,k2]
                k2 = -1
        if kk == [0,0]:
            k1 = -1
            k2 = -1
            for k in board:
                k1 = k1 + 1
                for kk in board[k1]:
                    k2 = k2 + 1
                    if board[k1][k2] == None:
                        return [k1,k2]
                k2 = -1
        k2 = -1
    print("stopededminimax")
    return [kk[0],kk[1]]
def nott(wh):
    if wh == 2:
        return 0
    elif wh == 0:
        return 2
