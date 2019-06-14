#!/usr/bin/env python

from utilities import *

def Euclid(state,problem):
    y1,x1 = state
    y2,x2 = problem.end_state
    return (y1-y2)**2+(x1-x2)**2

def Euclid3D(state,problem):
    z1, y1,x1 = state
    z2, y2,x2 = problem.end_state
    return (y1-y2)**2+(x1-x2)**2 + (z1-z2)**2

def traverse(problem,heuristic=Euclid):
    n = Node(state=problem.start_state,parent=None,path_cost=0)

    frontier = PriorityQueue()
    frontier.push(n,n.path_cost+heuristic(n.state,problem))
    explored = []
    while not frontier.isEmpty():
        n = frontier.pop()
        if n.state in explored:
            continue
        else:
            explored.append(n.state)
            if problem.end_state == n.state:
                return n.solution
            else:
                children = n.getChild(problem)
                for child in children:
                    frontier.push(child,child.path_cost+heuristic(child.state,problem))
 
    return 'Error'

def convertSolutionToMatrix(solution,problem):
    output = [[0]*len(problem.grid) for _ in xrange(len(problem.grid))]
    for y,x in solution:
        output[x][y] = 1
    printMatrix(output)

def convertSolutionToMatrix3D(solution,problem):
    output = [[[0]*len(problem.grid) for _ in xrange(len(problem.grid))]for _
              in xrange(len(problem.grid))]
    for z,y,x in solution:
        output[x][y][z] = 1
    printMatrix3D(output)

