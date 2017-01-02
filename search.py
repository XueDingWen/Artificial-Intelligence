"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def genericSearch(problem, fringe, decisionType, heuristic):
    goalCount = 0
    winAmount = 4

    startState = problem.getStartState()
    if decisionType == 0:
        fringe.push((startState, [], 0)) #DFS and BFS is DECISION 0
    elif decisionType == 1 or 2:
        fringe.push((startState, [], 0), 0) #UCS/A* SEARCH is DECISION 1
    visitedNodes = [] #actions
    pathTaken = []



    #WHILE LOOP HAS TWO SETTINGS
    while not fringe.isEmpty():
        #Once the fringe (the data structure) is empty, the search is over
        currentNode, path, costHere = fringe.pop()
        #we pop the node when there are no more children to visit

        #FOUND GOAL
        if problem.isGoalState(currentNode):
            #Check for the goal state FIRST out of the two operations (goal?, visited?)
                pathTaken = path #to be returned later in the functino
                break

        #NO GOAL FOUND AT THIS POSITION
        #NOT VISITED YET
        if not visitedNodes.count(currentNode):
            #will return a value of 0 if currentNode is not found in visited Nodes
            #this will tell us if we have been to the node before
            visitedNodes.append(currentNode)
            #If we have not visited, add it to the list of visited nodes
            NextPathSuccessor = problem.getSuccessors(currentNode) #successors
            #Extracts data from NPS
            for NP in range(0,len(NextPathSuccessor)):
                #Raw data is lots of tuples! (Note for myself)
                (nextNode, direction, cost) = NextPathSuccessor[NP]
                if not (visitedNodes.count(nextNode)):
                    #Push to the data structure any children that haven't been visited
                    if decisionType == 0:
                        fringe.push((nextNode, (path+[direction]), (costHere+cost))) #BFS/DFS
                    elif decisionType == 1:
                        fringe.push((nextNode, (path+[direction]), (costHere+cost)), (costHere+cost)) #UCS
                    elif decisionType == 2:
                        fringe.push((nextNode, (path+[direction]), (costHere+cost)), (costHere+cost+heuristic(nextNode, problem))) #A*

    return pathTaken


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    #print "XX Depth First Search is enabled! please work!"
    #print "Now we can see the data that is streaming in:"
    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())
    #util.raiseNotDefined()
    """ Will quit the program if method not implemented"""
    #print "Creating the fringe (nodes waiting in a queue to be explored, LIFO queue puts successors in front)"
    fringe = util.Stack()
    #print "calling the generic search algorithm with a stack data structure!"
    DFS = genericSearch(problem, fringe, 0, 0)


    return DFS

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    fringe = util.Queue()
    return genericSearch(problem, fringe, 0, 0) # the 0 is for BFS/DFS
    #print "BFS enabled, please work!"

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #fringe = util.PriorityQueue()
    #fringe = util.PriorityQueueWithFunction():
    #return genericSearch(problem, fringe, 0,0)

    #HOW TO IMPLEMENT?
    frontier = util.PriorityQueue()
    return genericSearch(problem, frontier,1,0)
    #return genericSearch(problem, fringe, 1, 0) # the 1 is for UCS

    #util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    #fringe = util.PriorityQueue()
    fringe = util.PriorityQueue()
    return genericSearch(problem, fringe, 2,heuristic)
    #util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch