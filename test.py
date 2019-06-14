#!/usr/bin/env python

import search
from utilities import Problem,printMatrix, Problem3D, printMatrix3D

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

    print ""
    print ""
    print "3D"
    print ""
    
    grid3D = [[[1,0,0],\
             [1,0,1],\
             [0,1,0]],\

            [[0,1,0],\
             [1,0,1],\
             [1,1,0]],\

            [[0,1,1],\
             [1,0,0],\
             [0,1,1]]];
    start_state3 = (0,0,0);
    end_state3 = (1,2,1);
    p3 = Problem3D(grid3D,start_state3,end_state3)
    path3 = search.traverse(p3,search.Euclid3D)

    printMatrix3D(grid3D)
    print(path3)
    search.convertSolutionToMatrix3D(path3,p3)
