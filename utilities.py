#!/usr/bin/env python
import heapq

class Problem:
    def __init__(self,grid,start_state,end_state):
        self.start_state = start_state;
        self.end_state = end_state;
        self.grid = grid;
        self.actions = ["left","right","forward","backward"]

    def isLegalState(self,state):
        y,x = state
        if x>=len(self.grid) or y>= len(self.grid) or x<0 or y < 0 or self.grid[x][y] == 0:
            return False
        else:
            return True

    def getSuccessors(self,state):
        children = [];
        y,x = state
        for action in self.actions:
            if action == "left":
                child_state = (y,x-1)
            elif action == "right":
                child_state = (y,x+1)
            elif action == "forward":
                child_state = (y+1,x)
            elif action == "backward":
                child_state = (y-1,x)
            if self.isLegalState(child_state):
                children.append(child_state)
        return children

    def getCostOfAction(self,solution):
        path_cost = 0;
        for state, next_state in zip(solution, solution[1:]):
            y1,x1 = state
            y2,x2 = next_state
            path_cost += (x1-x2)**2+(y1-y2)**2
        return path_cost

class Node:
    def __init__(self,state=None,parent=None,path_cost=0):
        self.state = state
        self.path_cost = path_cost
        self.parent = parent

        self.solution = [self.state]

        if self.parent is None:
            self.solution = []
        else:
            self.solution = parent.solution + self.solution

    def getChild(self,problem):
        children = []
        for successor in problem.getSuccessors(self.state):
            child = Node(state=successor,parent=self)
            child.path_cost = problem.getCostOfAction(child.solution)
            children.append(child)
            children.sort(key=lambda x: x.path_cost)
        return children


class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.count = 0

    def push(self, item, priority):
        entry = (priority, self.count, item)
        heapq.heappush(self.heap,entry)
        self.count += 1

    def pop(self):
        (_,_,item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0

    def update(self,item, priority):
        for index, (p,c,i) in enumerate(self.heap):
            if i== item:
                if p <= priority:
                    break
                del self.heap[index]
                self.heap.append((priority,c,item))
                heapq.heapify(self.heap)
                break
            else:
                self.push(item,priority)

def printMatrix(matrix):
    for row in matrix:
        for c in row:
            print c ,
        print ""
