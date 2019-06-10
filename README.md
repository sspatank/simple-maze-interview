# Simple Maze Problem

## Evaluation Criteria 
* Correctness of the solution 
* Simplicity and clarity of code
* Turn around time


# Problem 1

Given a maze as N*N binary matrix of blocks and the source and destination blocks as the coordinates (Xs, Ys) and (Xd, Yd). Build a utility that would allow a robot to start from source and find path to reach the destination. The robat can move in four directions (left, right, forward, back) as long as the path is clear.
In the maze matrix, 0 means the position is a dead end and 1 means the position can be used in the path from source to destination. 

Following is binary matrix representation of the above maze and the source and destination positions.
```
#Source
(0, 4)

#Destination 
(4, 2)

#Matrix
{1, 0, 0, 0, 0}
{1, 1, 1, 1, 1}
{0, 1, 0, 0, 1}
{1, 1, 1, 1, 0}
{1, 1, 1, 1, 1}
```

Following is the solution matrix (output of program) for the above input matrx.
```
#Matrix
{0, 0, 0, 0, 0}
{0, 1, 1, 1, 1}
{0, 1, 0, 0, 1}
{0, 1, 0, 0, 0}
{1, 1, 0, 0, 0}

# All enteries in solution path are marked as 1.
```

Write a utility that can take a matrix, source and destination and return a **valid** path between source and destination. 


# Extra Credit Problem

Given a 3D maze as N*N*N binary matrix of blocks and the source and destination blocks as the coordinates (Xs, Ys, Zs) and (Xd, Yd, Zd). Build a utility that would allow a drone to start from source and find a flight path to reach the destination. The drone can move in six directions (left, right, forward, back, up, down) as long as the path is clear.
