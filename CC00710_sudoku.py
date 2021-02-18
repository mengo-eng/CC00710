# Assignment 007/10 - C7185-Elnur
# Write a Python code to print out the given sudoku puzzle matrix in the following format.
sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]

for i in range(len(sudoku)+1):
    for j in range(len(sudoku)):
        if i == len(sudoku):
            break
        if j ==3 or j ==7:
            sudoku[i][j:j] = ["|"]
    if i % 3 == 0 or i == len(sudoku):
        print("_ "*2*(len(sudoku)-1))
        if i == len(sudoku):
            break

    print(*sudoku[i], sep ="  ")