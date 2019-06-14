#!/usr/bin/env python

import search
from utilities import Problem,printMatrix, Problem3D, printMatrix3D

# Run the tests
if __name__ == "__main__":

    #Grid 1: 2D grid
    grid = [[1,0,0,0,0],\
            [1,1,1,1,1],\
            [0,1,0,0,1],\
            [1,1,1,1,0],\
            [1,1,1,1,1]];
    start_state = (0,4);
    end_state = (4,2);
    
    #Problem object saves the grid and the start and end states
    p = Problem(grid,start_state,end_state)

    # Traverse uses A* to output a list of tuples with the coordinates of the
    # solution path
    path = search.traverse(p)

    # Prints the input grid
    printMatrix(grid)

    # Print the solution path
    print(path)

    #Print the solution grid
    search.convertSolutionToMatrix(path,p)

    print ""
    print ""

    #Grid 2: 3D grid

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
