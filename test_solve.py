sudoku = [['5', '3', '', '', '7', '', '', '', ''], 
          ['6', '', '', '1', '9', '5', '', '', ''],
          ['', '9', '8', '', '', '', '', '6', ''],
          ['8', '', '', '', '6', '', '', '', '3'],
          ['4', '', '', '8', '', '3', '', '', '1'],
          ['7', '', '', '', '2', '', '', '', '6'],
          ['', '6', '', '', '', '', '2', '8', ''],
          ['', '', '', '4', '1', '9', '', '', '5'],
          ['', '', '', '', '8', '', '', '7', '9']]


def get_empty_cells(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '':
                return (i, j)
    

def solve(grid):
    empty_cell = get_empty_cells(grid)
    if not empty_cell:
        return True
    else:
        row, col = empty_cell
    for i in range(1, 10):
        if check(grid, i, row, col):
            grid[row][col] = str(i)
            if solve(grid):
                return True
            grid[row][col] = ''
    return False


def check(grid, i, row, col):
    if str(i) in grid[row]:
        return False

    for j in range(9):
        if grid[j][col] == str(i):
            return False
    
    start_row = row - row % 3
    start_col = col - col % 3
    for m in range(3):
        for n in range(3):
            if grid[m + start_row][n + start_col] == str(i):
                return False
    return True

solve(sudoku)
print(*sudoku, sep='\n')