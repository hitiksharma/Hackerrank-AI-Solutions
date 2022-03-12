import sys
import math
sys.setrecursionlimit(100000)    # Set recursion depth to 10^5

POSMAP = {1:(0,0), 2:(0,3), 3:(0,6), 4:(1,1), 5:(1,3), 6:(1,5), 7:(2,2), 8:(2,3), 9:(2,4),
   10:(3,0), 11:(3,1), 12:(3,2), 13:(3,4), 14:(3,5), 15:(3,6), 16:(4,2), 17:(4,3), 18:(4,4),
   19:(5,1), 20:(5,3), 21:(5,5), 22:(6,0), 23:(6,3), 24:(6,6)}
POINTMAP = {(0,0):1, (0,3):2, (0,6):3, (1,1):4, (1,3):5, (1,5):6, (2,2):7, (2,3):8, (2,4):9,
  (3,0):10, (3,1):11, (3,2):12, (3,4):13, (3,5):14, (3,6):15, (4,2):16, (4,3):17, (4,4):18,
  (5,1):19, (5,3):20, (5,5):21, (6,0):22, (6,3):23, (6,6):24}
TRI = ((1,2,3),(4,5,6),(7,8,9),(10,11,12),(13,14,15),(16,17,18),(19,20,21),(22,23,24),
       (1,10,22),(3,15,24),(4,11,19),(6,14,21))
ADJACENT = {1:(2,10), 2:(1,3,5), 3:(2,15), 4:(5,11), 5:(2,4,6,8), 6:(5,14), 7:(8,12),
       8:(5,7,9), 9:(8,13), 10:(1,22,11), 11:(4,10,12,19), 12:(7,11,16), 13:(9,14,18),
       14:(6,13,15,21), 15:(3,14,24), 16:(12,17), 17:(16,18,20), 18:(13,17),
       19:(11,20), 20:(17,19,21,23), 21:(14, 20), 22:(10,23), 23:(20,22,24), 24:(15,23)}
EMPTYCELL = 'O'
WALL = ['|', '*']
COEFF = [18, 26, 5, 6, 12, 7, 14, 43, 10, 8, 7, 42, 1086, 10, 1, 16, 1190]
bboard =[]
prevBoard = []
best_move = POSMAP[1]   # Change during each next_move call

def mmp(val):
    global POSMAP, bboard
    return bboard[POSMAP[val][0]][POSMAP[val][1]]
    
def closedMorris(board):
    global player, opponent, bboard
    global POSMAP, POINTMAP, EMPTYCELL, WALL, TRI
    bboard = board
    for tri in TRI:
        if mmp(tri[0]) == mmp(tri[1]) == mmp(tri[2]) == player:
            return True
    return False

def numclosedmorris(board, player):
    global bboard
    global POSMAP, POINTMAP, EMPTYCELL, WALL, TRI
    bboard = board
    num = 0
    for tri in TRI:
        if mmp(tri[0]) == mmp(tri[1]) == mmp(tri[2]) == player:
            num += 1
    return num

def twopieces(board):
    global player, opponent, bboard
    global POSMAP, POINTMAP, EMPTYCELL, WALL
    bboard = board
    for tri in TRI:
        tris = map(mmp, tri)
        if tris.count(player) == 2 and EMPTYCELL in tris:
            return True
    return False

def morrisnumber(board):
    global player, opponent, bboard
    global POSMAP, POINTMAP, EMPTYCELL, WALL
    bboard = board
    num = 0
    for tri in TRI:
        tris = map(mmp, tri)
        if tris.count(player) == 2 and EMPTYCELL in tris:
            num += 1
    return num

def opponentblock(board):
    global player, opponent, bboard
    global POSMAP, POINTMAP, EMPTYCELL, WALL
    bboard = board
    num = 0
    for tri in TRI:
        tris = map(mmp, tri)
        if opponent in tris and player in tris:
            num += tris.count(opponent)
    return num

def piecesnumber(board):
    global player, opponent, bboard
    global POSMAP, POINTMAP, EMPTYCELL, WALL
    bboard = board
    pieces = 0
    for point in xrange(1, len(POSMAP)+1):
        if mmp(point) == player:
            pieces += 1
    return pieces

def openedmorris(board):
    global player, opponent, bboard, prevBoard
    global POSMAP, POINTMAP, EMPTYCELL, WALL
    if numclosedmorris(prevBoard, opponent) > numclosedmorris(board, opponent):
        return True
    return False

def closedmorris(board):
    global player, opponent, bboard, prevBoard
    global POSMAP, POINTMAP, EMPTYCELL, WALL
    if numclosedmorris(prevBoard, player) < numclosedmorris(board, player):
        return True
    return False

def estimator(board):
    ''' Basic estimator '''
    global player, opponent, phase, prevBoard
    global POSMAP, POINTMAP, EMPTYCELL, WALL, COEFF
    #print 'pieces', piecesnumber(board)
    #print 'closed', closedMorris(board)
    #print 'two', twopieces(board)
    #print 'morrisnum', morrisnumber(board)
    #print 'opp block', morrisnumber(board)
    #print 'closed new', closedmorris(board)
    if phase == "INIT":
        return piecesnumber(board)*COEFF[3] + int(closedMorris(board))*COEFF[0] + int(twopieces(board))*COEFF[4]\
           + int(morrisnumber(board))*COEFF[1] + opponentblock(board)*COEFF[2] + closedmorris(board)*20
    else:
        return int(closedMorris(board))*COEFF[6] + int(morrisnumber(board))*COEFF[7] + opponentblock(board)*COEFF[8]\
           + piecesnumber(board)*COEFF[9] + int(closedmorris(board))*100 + int(openedmorris(board))*COEFF[10]

def alphabetapruning(board, cplayer, copponent, depth, maxdepth, alpha, beta):
    global POSMAP, POINTMAP, EMPTYCELL, WALL, ADJACENT
    global player, opponent, best_move, phase
    if depth == 0:
        estimate = estimator(board)
        if board[1][5] == player or board[5][3] == player:
            print estimate, cplayer
            print '\n'.join(''.join(b) for b in board)
            print
        return estimate
    for point, pos in POSMAP.iteritems():
        if board[pos[0]][pos[1]] == EMPTYCELL and phase == "INIT":
            board[pos[0]][pos[1]] = cplayer
            subalpha = alphabetapruning(board, copponent, cplayer, depth-1, maxdepth, alpha, beta)
            board[pos[0]][pos[1]] = EMPTYCELL
            if player == cplayer:
                if subalpha > alpha:    #maximize
                    alpha = subalpha
                    if beta <= alpha: break
                    if depth == maxdepth: best_move = POSMAP[point]
            else:    # opponent
                beta = min(subalpha, beta)
                if beta <= alpha: break
        elif board[pos[0]][pos[1]] == cplayer and phase == "MOVE":
            for adj in ADJACENT[point]:
                if board[POSMAP[adj][0]][POSMAP[adj][1]] == EMPTYCELL:
                    board[pos[0]][pos[1]] = EMPTYCELL
                    board[POSMAP[adj][0]][POSMAP[adj][1]] = cplayer
                    subalpha = alphabetapruning(board, copponent, cplayer, depth-1, maxdepth, alpha, beta)
                    board[POSMAP[adj][0]][POSMAP[adj][1]] = EMPTYCELL
                    board[pos[0]][pos[1]] = cplayer
                    if player == cplayer:
                        if subalpha > alpha:    #maximize
                            alpha = subalpha
                            if beta <= alpha: break
                            if depth == maxdepth:
                                best_move = (POSMAP[point][0], POSMAP[point][1], POSMAP[adj][0], POSMAP[adj][1])
                                #print board[POSMAP[adj][0]][POSMAP[adj][1]], POSMAP[adj][0], POSMAP[adj][1]
                                #print '\n'.join(''.join(b) for b in board)
                    else:    # opponent
                        beta = min(subalpha, beta)
                        if beta <= alpha: break
        elif board[pos[0]][pos[1]] == opponent and depth == maxdepth and phase == "MILL":
            board[pos[0]][pos[1]] = EMPTYCELL
            subalpha = alphabetapruning(board, copponent, cplayer, 0, maxdepth, alpha, beta)
            board[pos[0]][pos[1]] = opponent
            if player == cplayer:
                if subalpha > alpha:    #maximize
                    alpha = subalpha
                    if beta <= alpha: break
                    best_move = POSMAP[point]
            else:    # opponent
                beta = min(subalpha, beta)
                if beta <= alpha:
                    break
    if cplayer==player:
        return alpha
    return beta

def nextMove(player, opponent, phase, board):
    global best_move, prevBoard
    prevBoard = map(list, board)
    alpha = alphabetapruning(board, player, opponent, 2, 2, float("-inf"), float("inf"))
    for _ in best_move:
        print _,

if __name__ == "__main__":
    player = raw_input().strip()
    if player == "B": opponent = "W"
    else: opponent = "B"
    phase = raw_input().strip()
    board = []
    for x in xrange(7):
        board.append(list(raw_input()))
    nextMove(player, opponent, phase, board)
