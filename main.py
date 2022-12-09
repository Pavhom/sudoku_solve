import sys
import design
from PyQt5.QtWidgets import QLineEdit, QMainWindow, QApplication


class SudokuSolver(QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.sudoku = []
        self.pushButton.clicked.connect(self.clear_field)
        self.pushButton_2.clicked.connect(self.run)
    

    def clear_field(self):
        '''Clears the field from the entered values'''
        for cell in self.centralwidget.findChildren(QLineEdit):
            cell.clear()


    def get_values(self):
        '''Receives data from all cells of the field 
        and returns them in the form of a 9x9 matrix'''
        values_all = []
        values_row = []
        cell_values = {cell.objectName().lstrip('lineEdit_'): cell.text() for cell in self.centralwidget.findChildren(QLineEdit)}
        sorted_keys = sorted([int(key) for key in cell_values.keys()])
        
        for key in sorted_keys:
            values_row.append(cell_values[str(key)])
            if len(values_row) == 9:
                values_all.append(values_row)
                values_row = []
        return values_all


    def get_empty_cells(self, grid):
        '''On each call returns the coordinates of an empty cell. 
        The data is returned as a tuple with two values, row index and column index.'''
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '':
                    return (i, j)
        

    def solve(self, grid):
        '''The function sets the value to the empty cell being processed 
        and continues the solution by calling itself. 
        The action is repeated until there are empty cells, 
        or until the function returns false'''
        empty_cell = self.get_empty_cells(grid)
        if not empty_cell:
            return True
        else:
            row, col = empty_cell
        for i in range(1, 10):
            if self.check(grid, i, row, col):
                grid[row][col] = str(i)
                if self.solve(grid):
                    return True
                grid[row][col] = ''
        return False


    def check(self, grid, i, row, col):
        '''Checks a number for its presence in a row, column and 3x3 square'''
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


    def set_values(self):
        '''generates one list of all values in the sudoku variable, 
        also a dictionary where the value is the objectname of the cell and the key is the cell number. 
        Displays values in gui'''
        cell_values = {cell.objectName().lstrip('lineEdit_'): cell.objectName() for cell in self.centralwidget.findChildren(QLineEdit)}
        sorted_keys = sorted([int(key) for key in cell_values.keys()])
        output_values = []
        
        for line in self.sudoku:
            output_values.extend(line)
    
        for i in range(len(sorted_keys)):
            self.centralwidget.findChild(QLineEdit, f'lineEdit_{sorted_keys[i]}').setText(output_values[i])
        

    def run(self):
        self.sudoku = self.get_values()
        self.solve(self.sudoku)
        self.set_values()
        

def main():
    app = QApplication(sys.argv)
    window = SudokuSolver()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()