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

def depthFirstSearch(problem):
  "*** YOUR CODE HERE ***"
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  
  visited = set()
  raiz = problem.getStartState()
  pilha = util.Stack()


  # A ideia aqui e ter um Value Object que ira representar um objeto que possui apenas as informacoes necessarias formatadas
  # para meu problema. Usando o padrao VO consigo um codigo mais limpo e facil de debugar. 
  # Esse VO possui 3 caracteristicas: action (norte, sul, leste e oeste), state (o estado do no no plano cartesiano), 
  # e parent (caminho que levou ate ele). Dessa forma, posso mapear o caminho que levou ate o no destino, tendo as acoes, e 
  # retornando a solucao para o melhor caminho.  
  
  nodeVO = {}
  pilha.push(_getStartState(nodeVO, raiz, 0, 0))

  while not pilha.isEmpty():
    # print nodeVO
    nodeVO = pilha.pop()
    atual = nodeVO["node"]
    if atual in visited:
      continue
    visited.add(atual)

    # Momento em que paramos nossa busca, pois ja temos o caminho
    if problem.isGoalState(atual) == True:
      break

    for child in problem.getSuccessors(atual):
      if not child[0] in visited:
        subNode = {}
        pilha.push(_createSubNode(subNode, nodeVO, child, 0, 0, 0))

  actions = []
  while nodeVO["action"] != None:
    actions.insert(0, nodeVO["action"])
    nodeVO = nodeVO["parent"]
    
  return actions


#   ********************************************************************************************************

def breadthFirstSearch(problem):
    "*** YOUR CODE HERE ***"
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    print problem

    fila = util.Queue()
    visited = set()
    raiz = problem.getStartState()

    nodeVO = {}
    fila.push(_getStartState(nodeVO, raiz, 0, 0))
    # Uso aqui o mesmo padrao da busca anterior, formatando minhas informacoes em um value object, e encadiando seu caminho na propriedade parent
    while not fila.isEmpty():
        # print nodeVO
        nodeVO = fila.pop()
        atual = nodeVO["node"]
        if atual in visited:
            continue

        visited.add(atual)
        # Momento em que paramos nossa busca, pois ja temos o caminho
        if problem.isGoalState(atual) == True:
            break

        for child in problem.getSuccessors(atual):
            if child[0] not in visited:
                subNode = {}
                fila.push(_createSubNode(subNode, nodeVO, child, 0, 0, 0))

    actions = []
    while nodeVO["action"] != None:
        actions.insert(0, nodeVO["action"])
        nodeVO = nodeVO["parent"]

    return actions

#   ********************************************************************************************************

def uniformCostSearch(problem):
    "*** YOUR CODE HERE ***"
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    print problem

    filaPrior = util.PriorityQueue()
    visited = set()

    # Uso aqui o mesmo padrao da busca anterior, formatando minhas informacoes em um value object, e encadiando seu caminho na propriedade parent
    # Na fila de prioridade, uso o custo para alcancar o proximo no como classificador

    raiz = problem.getStartState()
    nodeVO = {}
    filaPrior.push(_getStartState(nodeVO, raiz, 0, 1), nodeVO["cost"])

    while not filaPrior.isEmpty():
        # print nodeVO
        nodeVO = filaPrior.pop()
        atual = nodeVO["node"]
        cost = nodeVO["cost"]

        if atual in visited:
            continue

        visited.add(atual)
        if problem.isGoalState(atual) == True:
            break

        for child in problem.getSuccessors(atual):
            if child[0] not in visited:
                subNode = {}
                filaPrior.push(_createSubNode(subNode, nodeVO, child, cost, 0, 1), subNode["cost"])

    actions = []
    while nodeVO["action"] != None:
        actions.insert(0, nodeVO["action"])
        nodeVO = nodeVO["parent"]

    return actions


# ********************************************************************************************

def nullHeuristic(state, problem=None):
    return 0


# ********************************************************************************************

def aStarSearch(problem, heuristic=nullHeuristic):
    "*** YOUR CODE HERE ***"
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    print problem

    filaPrior = util.PriorityQueue()
    visited = set()

    # Uso aqui o mesmo padrao da busca anterior, formatando minhas informacoes em um value object, e encadiando seu caminho na propriedade parent
    # Na fila de prioridade, uso a heuristica e o custo para alcancar o proximo no como classificadores. A heuristica vem do metodo nullHeuristic =)...

    raiz = problem.getStartState()
    heuristica = heuristic(raiz, problem)

    nodeVO = {}
    filaPrior.push(_getStartState(nodeVO, raiz, heuristica, 2), nodeVO["cost"] + nodeVO["heuristic"])

    while not filaPrior.isEmpty():
        nodeVO = filaPrior.pop()
        atual = nodeVO["node"]
        cost = nodeVO["cost"]
        v = nodeVO["heuristic"]
        #print nodeVO
        if atual in visited:
            continue

        visited.add(atual)

        if problem.isGoalState(atual) == True:
            break

        for child in problem.getSuccessors(atual):
            if child[0] not in visited:
                subNode = {}
                heuristicaSubNode = heuristic(child[0], problem)
                _createSubNode(subNode, nodeVO, child, cost, heuristicaSubNode, 2)
                filaPrior.push(_createSubNode(subNode, nodeVO, child, cost, heuristicaSubNode, 2), subNode["cost"] + nodeVO["heuristic"])

    actions = []
    while nodeVO["action"] != None:
        actions.insert(0, nodeVO["action"])
        nodeVO = nodeVO["parent"]

    return actions

# ********************************************************************************************

def printStack(stack):
    print "Pilha no final do exercicio:"
    stackAux = stack
    while not stackAux.isEmpty():
        print stackAux.pop()

def _getStartState(nodeVO, raiz, heuristic, variations):
    if variations == 0:
        nodeVO["parent"] = None
        nodeVO["action"] = None
        nodeVO["node"] = raiz
    if variations == 1:
        nodeVO["parent"] = None
        nodeVO["action"] = None
        nodeVO["node"] = raiz
        nodeVO["cost"] = 0
    if variations == 2:
        nodeVO["parent"] = None
        nodeVO["action"] = None
        nodeVO["node"] = raiz
        nodeVO["cost"] = 0
        nodeVO["heuristic"] = heuristic
    return nodeVO

def _createSubNode(subNode, nodeVO, child, cost, heuristic, variations):
    if variations == 0:
        subNode["parent"] = nodeVO
        subNode["action"] = child[1]
        subNode["node"] = child[0]
    if variations == 1:
        subNode["parent"] = nodeVO
        subNode["node"] = child[0]
        subNode["action"] = child[1]
        subNode["cost"] = child[2] + cost
    if variations == 2:
        subNode["parent"] = nodeVO
        subNode["node"] = child[0]
        subNode["action"] = child[1]
        subNode["cost"] = child[2] + cost
        subNode["heuristic"] = heuristic
    return subNode


def learningRealTimeAStar(problem, heuristic=nullHeuristic):
    """Execute a number of trials of LRTA* and return the best plan found."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

    # MAXTRIALS = ...
    

# Abbreviations 
# *** DO NOT CHANGE THESE ***
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
lrta = learningRealTimeAStar
