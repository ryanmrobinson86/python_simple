#
# buckets.py
#
# a simple module to solve the bucket algorithm by tree search
#
import string, sys

class manager:
    " Manage the process queue and keep track of states already seen, and manage relations among states"
    def __init__(self):
        self.queue = []
        self.parents = {}

    def getState(self):
        "return next state and pop it off the queue"
        if not self.queue:
            return None
        state = self.queue[0]
        self.queue = self.queue[1:]
        return state

    def addState(self, parentState, newState):
        """add state if it's new, remember it's parent. if there's already an entry in
		the parents dictionary then we've seen this state before."""
        if self.parents.has_key(str(newState)):
            return
        self.parents[str(newState)] = str(parentState)
        self.queue.append(newState)
        #print '--- Adding ', newState, "<--- ", parentState

    def getSolution(self):
        "return solution from latest state added"
        solution = []
        state = self.queue[-1]
        while state:
            solution.append(str(state))
            state = self.getParent(state)
        solution.reverse()
        return solution

    def getParent(self, childState):
        "return parent of the childState"
        try:
            return self.parents[str(childState)]
        except:
            return None

class bucket:
    def __init__(self, manager):
        self.manager = manager

    def test(self, oldstate, newstate):
        [newA, newB] = newstate
        won = (newA == self.goal or newB == self.goal)
        self.manager.addState(oldstate, newstate)
        return won

    def play(self, aMax, bMax, goal):
        "grab a state and generate 8 more to submit to the manager"
        self.goal = goal
        self.manager.addState("", [0,0])
        while 1:
            oldstate = self.manager.getState()
            if not oldstate:
               print "No Solution" 
               return
            [aHas,bHas] = oldstate
            if self.test(oldstate, [aMax,bHas]):
                break
            if self.test(oldstate, [0,bHas]):
                break
            if self.test(oldstate, [aHas,bMax]):
                break
            if self.test(oldstate, [aHas,0]):
                break
            howmuch = min(aHas, bMax-bHas)
            if self.test(oldstate, [aHas-howmuch,bHas+howmuch]):
                break
            howmuch = min(bHas, aMax-aHas)
            if self.test(oldstate, [aHas+howmuch,bHas-howmuch]):
                break
        print "Solution is"
        print string.join(self.manager.getSolution(), "\n")
