#
# towers.py
#
# OO solution to the towers of hanoi game
#
import string

class counter:
    def __init__(self):
        self.tot = 0

class disk:
    def __init__(self,name,nextSmaller,accum):
        self.name = name
        self.peg = 1
        self.nextSmaller = nextSmaller
        self.moves = accum

    # the approach taken here is to check if there are any smaller
    # than myself; if so, ask them to move to the alternate peg, once that
    # is done, I can move myself to the new peg and ask the one smaller
    # than me to move to the new peg on top of me.
    def move(self, newPeg):
        print self.name,": I have been asked to move to peg", newPeg
        if self.nextSmaller:
            # figure out which peg is the alternate
            pegs = [1,2,3]
            # remove the one I'm on
            pegs.remove(self.peg)
            # remove the one I want to move to
            pegs.remove(newPeg)
            # this is the only one left
            altPeg = pegs[0]

            # ask the next smaller one to move to the alternate peg
            print self.name, ": Asking", self.nextSmaller.name, "to get out of the way"
            self.nextSmaller.move(altPeg)

            #move myself to the new peg
            print self.name, ": Moving to", newPeg
            self.peg = newPeg
            self.moves.tot += 1

            #ask the next smaller to move on top of me
            print self.name, ": Asking ", self.nextSmaller.name, " to move on top of me"
            self.nextSmaller.move(newPeg)
        else:
            # i'm the smallest, so just move
            print self.name, ": Moving to", newPeg
            self.peg = newPeg
            self.moves.tot += 1
    
# after I noticed the pattern had a mathematical solution the the number of moves
# required, I made this method to calculate the number of moves only.  Much faster than
# the brute force method.
def solve(disks):
	return 2**disks - 1

# allow the user to specify the number of disks
def play(p,disks):
	d = []
	c = counter()
	if p:
		for i in range(disks):
			n = i + 1
			name = "D%d" % n
			try:
				d.append(disk(name,d[-1],c))
			except:
				d.append(disk(name,None,c))
			print "Created disk ",name
		d[-1].move(3)
	else:
		c.tot = solve(disks)
		
	print "It took ", c.tot, " moves to solve."