# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import queue

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

class Node:
    def __init__(self, state,action , cost = 0):
        self.state = state
        self.action = action
        self.cost = cost



def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:"""

    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    "*** YOUR CODE HERE ***"

    node = Node(problem.getStartState(),[])
    # if problem.isGoalState(node.state):
    #     return []

    frontier = util.Stack()
    frontier.push(node)

    reached = set()

    while not frontier.isEmpty():
        node = frontier.pop()

        if problem.isGoalState(node.state):
            return node.action

        if node.state not in reached:
            reached.add(node.state)

        for child in problem.getSuccessors(node.state):
            child_node = Node(child[0],[],child[2])

            if child_node.state not in reached:
                child_node.action = node.action + [child[1]]
                frontier.push(child_node)
    return []

    #util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    node = Node(problem.getStartState(),[])
    # if problem.isGoalState(node.state):
    #     return []

    frontier = util.Queue()
    frontier.push(node)

    reached = list()
    reached.append(node.state)

    while not frontier.isEmpty():
        node = frontier.pop()

        if problem.isGoalState(node.state):
            return node.action


        for child in problem.getSuccessors(node.state):
            child_node = Node(child[0],[],child[2])

            if child_node.state not in reached:
                reached.append(child_node.state)
                child_node.action = node.action + [child[1]]
                frontier.push(child_node)

    return []

    #util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    node = Node(problem.getStartState(),[],0)

    frontier = util.PriorityQueue()
    frontier.push(node, node.cost)

    reached = set()

    while not frontier.isEmpty():
        node = frontier.pop()

        if problem.isGoalState(node.state):
            return node.action

        if node.state not in reached:
            reached.add(node.state)

            for child in problem.getSuccessors(node.state):
                child_node=Node(child[0],[])

                if child_node.state not in reached:
                  child_node.action = node.action + [child[1]]
                  child_node.cost = node.cost + child[2]
                  #print(child_node.cost)
                  frontier.push(child_node, child_node.cost)

    return []



    #util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """

    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    node = Node(problem.getStartState(), [], 0)

    frontier = util.PriorityQueue()
    frontier.push(node, node.cost)

    reached = list()

    while not frontier.isEmpty():
        node = frontier.pop()

        if problem.isGoalState(node.state):
            return node.action

        if node.state not in reached:
            reached.append(node.state)

            for child in problem.getSuccessors(node.state):
                child_node = Node(child[0], [])

                if child_node.state not in reached:
                    child_node.action = node.action + [child[1]]
                    child_node.cost = node.cost + child[2]
                    totalCost = child_node.cost + heuristic(child_node.state,problem)
                    frontier.push(child_node, totalCost)

    return []

    #util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
