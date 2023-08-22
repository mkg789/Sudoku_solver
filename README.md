# Sudoku_solver
A Python code to solve any 9x9 sudoku problem
The code has 2 functions defined: Validate and Solver.
The Validate function checks if there is any number repeated in the row, col, and grid. if there is any number repeated then it will return false, otherwise it will return true.
The Solver function is a recursive function that has backtracking to solve the sudoku problem.
To check if the code is working use this input to verify in a Python interpreter.
0,0,5,0,1,0,0,3,9
0,0,0,0,0,0,0,0,0
1,0,0,0,0,0,0,0,0
0,0,0,0,0,0,0,0,1
2,0,0,0,0,0,0,0,0
0,0,0,0,0,0,0,9,0
0,0,0,0,0,0,0,0,0
0,0,0,0,0,0,0,0,0
0,0,0,0,0,0,0,0,0
