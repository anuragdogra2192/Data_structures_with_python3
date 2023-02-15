'''
Using recursion
'''
import numpy as np

# Need a function to check a possibilty to add a number n or not

def possible(grid, y, x, n):
    for i in range(0,9):#Checking all possibilities in a particular row (moving in a column)
        if grid[y][i] == n:
            return False
    
    for i in range(0,9):#Column Check
        if grid[i][x] == n:
            return False
    
    #Calulating the sub-grid(3X3) coordinate
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    #Checking in the sub-grid
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == n:
                return False
    
    return True

def solver(grid):
    for y in range(0,9):
        for x in range(0,9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if possible(grid, y,x,n):
                        grid[y][x] = n
                        if solver(grid):
                            return True
                        grid[y][x]=0   
                return False
    print(np.matrix(grid))


# Grid 9 X 9 => y = Row, x = Column
grid = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
        [0, 1, 0, 0, 0, 4, 0, 0, 0],
        [4, 0, 7, 0, 0, 0, 2, 0, 8],
        [0, 0, 5, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 8, 1, 0, 0],
        [0, 4, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 3, 6, 0, 0, 7, 2],
        [0, 7, 0, 0, 0, 0, 0, 0, 3],
        [9, 0, 3, 0, 0, 0, 6, 0, 4]]
print(np.matrix(grid))

solver(grid)
