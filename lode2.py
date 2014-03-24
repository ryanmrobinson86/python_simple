#!/usr/bin/python
#
# lode2.py
#
import time,ttyLinux
from util import *

class Player:
    def setDirection(self, ch):
        pass

    def move(self):
        global inPlay, you
        spot = getSpot(self.row,self.col)
        lspot = getSpot(self.row,self.col-1)
        rspot = getSpot(self.row,self.col+1)

        horz,vert = self.dir
        writeScreen(self.row,self.col,spot)
        if spot == '_':
            self.col += horz
        elif spot == '|':
            self.row -= vert
        elif spot == ' ':
            self.row += 1
        if lspot == '_' and horz == -1:
            self.col -= 1
        elif rspot == '_' and horz == 1:
            self.col += 1
        writeScreen(self.row,self.col,self.face)
        if self == you and self.row > 23:
            inPlay = 0

class You(Player):
    def __init__(self, Row=1, Col=10, Face='^'):
        self.row = Row
        self.col = Col
        self.face = Face
        self.dir = (0,0)

    def setDirection(self, ch):
        if ch == '\033[A':
            self.dir = (0,1)  # up
        elif ch == '\033[B':
            self.dir = (0,-1) # down
        elif ch == '\033[C':
            self.dir = (1,0)  # right
        elif ch == '\033[D':
            self.dir = (-1,0) # left

class Robot(Player):
    def __init__(self, Row=1, Col=12, Face='&'):
        self.row = Row
        self.col = Col
        self.face = Face
        self.dir = (0,0)

    def setDirection(self, ch):
        global inPlay, you
        #did we tag him?
        if you.row == self.row and you.col == self.col:
            inPlay = 0
        # same level -> run towards you
        if self.row == you.row:
            # are we to the left of the robot?
            if self.col > you.col:
                self.dir = (-1,0)
            elif self.col < you.col:
                self.dir = (1,0)
        else:
            me = getSpot(self.row,self.col)
            if me == '|':
                if self.row > you.row:
                    self.dir = (0,1)
                elif self.row < you.row:
                    self.dir = (0,-1)

def main():
    setBoard(0)
    try:
        ttyLinux.setSpecial()
        playGame()
    finally:
        ttyLinux.setNormal()

def playGame():
    global inPlay, you
    you = You()
    writeBoard()
    players = [you]
    clock = 0
    inPlay = 1
    while inPlay:
        clock += 1
        if clock == 40:
            players.append(Robot())
        time.sleep(.1)
        keys = ttyLinux.readLookAhead()
        for player in players:
            player.setDirection(keys)
            player.move()
        writeScreen(20,0,'')
    writeScreen(20,0,'')

if __name__ == "__main__":
    main()
