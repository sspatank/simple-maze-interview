#!/usr/bin/env python

import search
from utilities import Problem,printMatrix

if __name__ == "__main__":
    grid = [[1,0,0,0,0],\
            [1,1,1,1,1],\
            [0,1,0,0,1],\
            [1,1,1,1,0],\
            [1,1,1,1,1]];
    start_state = (0,4);
    end_state = (4,2);
    p = Problem(grid,start_state,end_state)
    path = search.traverse(p)

    printMatrix(grid)
    print(path)
    search.convertSolutionToMatrix(path,p)
