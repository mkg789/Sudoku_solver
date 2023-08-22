import numpy as np
sudoku = []
for i in range(0,9):
    inp=list(map(int,input().strip().split(',')))
    sudoku.append(inp)
def Validate(row,col,num):
    for i in range(0,9):
    #solve for row
        if(sudoku[i][col]==num):
            return False
    #solve for column
        if (sudoku[row][i] == num):
            return False
    #solve for grid
    gr = (row//3)*3
    gc = (col//3)*3
    for i in range(gr,gr+3):
        for j in range(gc,gc+3):
            if(sudoku[i][j]==num):
                return False
    return True
def Solver(row,col):
    if(row == 8 and col == 9): # win condition
        return True
    if(col==9):
        row+=1
        col=0
    if sudoku[row][col]>0:
        return Solver(row,col+1) #recurrsion
    for num in range(1,10):
        if(Validate(row,col,num)):
            sudoku[row][col]=num
            if(Solver(row,col+1)):
                return  True
        sudoku[row][col]=0 #backtracking
    return False
Solver(0,0)
print(np.matrix(sudoku))#prints the output in form of a matrix