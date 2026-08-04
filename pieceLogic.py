class Piece:
    def __init__(self,name):
        self.color = name[0]
        self.pType = name[1]

    def movement(self,row,col,state):
        if self.pType == 'P':
            return pawnmove(self.color,row,col,state)
        elif self.pType == 'B':
            return bishopmove(self.color,row,col,state)
        elif self.pType == 'N':
            return knightmove(self.color,row,col,state)
        elif self.pType =='Q':
            return queenmove(self.color,row,col,state)
        elif self.pType == 'K':
            return kingmove(self.color,row,col,state)
        elif self.pType =='R':
            return rookmove(self.color,row,col,state)
        return []

def onboard(row,col):
    if row>=0 and row<=7 and col<=7 and col>=0:
        return True
    else:
        return False

#Move limits for Queen, Bishop, Knight, Rook    
def valid_move(color,row,col,direction,state):
    moves = []
    for dr,dc in direction:
        r = row+dr
        c = col+dc
        while onboard(r,c):
            if(state[r][c]=='_'):
                moves.append((r,c))
            elif(state[r][c][0]!=color):
                moves.append((r,c))
                break
            else:
                break
            r+=dr
            c+=dc
    return moves

def pawnmove(color,row,col,state):
    moves=[]
    direction = -1
    start_row = 6
    if color == 'b':
        direction = 1
        start_row = 1
    #Forward movement
    if onboard(row+direction,col) and state[row+direction][col]=='_':
        moves.append((row+direction,col))
        if row==start_row and state[row+2*direction][col]=='_':
            moves.append((row+2*direction,col))
    
    #Diagonal capture
    for diagonal in [-1,1]:
        target_row, target_col = row+direction,col+diagonal
        target = state[target_row][target_col]
        if onboard(target_row,target_col) and target!='_' and target[0]!=color:
            moves.append((target_row,target_col))

    return moves

def bishopmove(color,row,col,state):
    direction = [(1,-1),(1,1),(-1,1),(-1,-1)]
    moves = valid_move(color,row,col,direction,state)
    return moves

def queenmove(color,row,col,state):
    direction = [(1,-1),(1,1),(-1,1),(-1,-1),(1,0),(0,1),(0,-1),(-1,0)]
    moves = valid_move(color,row,col,direction,state)
    return moves

def rookmove(color,row,col,state):
    direction = [(1,0),(0,1),(0,-1),(-1,0)]
    moves = valid_move(color,row,col,direction,state)
    return moves

def knightmove(color,row,col,state):
    moves = []
    offset = [
        (-2,1),(1,2),(2,-1),(-1,2),
        (-2,-1),(1,-2),(-1,-2),(2,1)
    ]
    for dr,dc in offset:
        r = row + dr
        c = col + dc
        if onboard(r,c):
            if(state[r][c]=='_' or state[r][c][0]!=color):
                moves.append((r,c))
    return moves

def kingmove(color,row,col,state):
    moves=[]
    direction = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,1),(-1,1),(1,-1)]
    for dr,dc in direction:
        r = row+dr
        c = col+dc
        if onboard(r,c):
            target = state[r][c]
            if target =='_' or target[0]!=color:
                moves.append((r,c))
    return moves