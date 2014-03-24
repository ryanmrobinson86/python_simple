#
# util.py
#
import sys, string, boards, copy

def setBoard(n):
    global board
    board = copy.copy(boards.boards[n])

def getSpot(row,col):
    'return board value ("_", "|", or " ") for row,col'
    try:
        return board[row][col]
    except:
        return ' '

def setSpot(row,col,newchar):
    'update board value at row,col with newchar'
    try:
        l = board[row]
        l = l[:col]+newchar+l[col+1:]
        board[row] = l
    except:
        pass

def writeBoard():
    'write entire board to the screen'
    global board
    sys.stdout.write('\033[1;1H\033[J')
    for row in range(len(board)):
        writeScreen(row, 0, board[row])

def writeScreen(row,col,char):
    'write a char to the screen and row,col'
    sys.stdout.write('\033[%d;%dH%s' % (row+1,col+1,char))
    sys.stdout.flush()
