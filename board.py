import pygame
from Cell import Cell


class Board:

    def __init__(self, width, height, screen, board_values, solution):
        """
       Initializes the Board with the given parameters.

       Parameters:
       - width (int): The width of the board in pixels.
       - height (int): The height of the board in pixels.
       - screen (pygame.Surface): The Pygame surface where the board will be drawn.
       - board_values (list of lists): A 2D list representing the initial state of the Sudoku board.
       - solution (list of lists): A 2D list representing the solved Sudoku board.
       """
        self.width = width
        self.height = height
        self.screen = screen
        self.selected_cell = None
        self.board_values = board_values
        self.solution = solution

        self.grid = [[Cell(self.board_values[row][col], row, col, screen) for col in range(9)] for row in range(9)]

    def draw(self):
        """
        Draws the board and all its cells onto the screen.
        """
        # Draw cells
        for row in range(9):
            for col in range(9):
                self.grid[row][col].draw()

        # Draw grid lines
        cell_size = 60
        for i in range(10):
            if i % 3 == 0:
                line_width = 4
            else:
                line_width = 1
            # Draw horizontal lines
            pygame.draw.line(self.screen, pygame.Color('black'), (0, i * cell_size), (self.width, i * cell_size),
                             line_width)
            # Draw vertical lines
            pygame.draw.line(self.screen, pygame.Color('black'), (i * cell_size, 0), (i * cell_size, self.height),
                             line_width)

    def select(self, row, col):
        """
       Marks the cell at (row, col) as the selected cell.

       Parameters:
       - row (int): The row index of the cell to select (0-8).
       - col (int): The column index of the cell to select (0-8).
       """
        if self.selected_cell:
            self.selected_cell.selected = False
        self.grid[row][col].selected = True
        self.selected_cell = self.grid[row][col]

    def click(self, x, y):
        """
        Determines which cell was clicked based on x and y coordinates.

        Parameters:
        - x (int): The x-coordinate of the mouse click.
        - y (int): The y-coordinate of the mouse click.

        Returns:
        - tuple: (row, col) if the click is within the board boundaries.
        - None: If the click is outside the board.
        """
        if x < self.width and y < self.height:
            return int(y // 60), int(x // 60)
        else:
            return None

    def sketch(self, value):
        """
        Sets the sketched value for the selected cell.

        Parameters:
        - value (int): The value to sketch in the selected cell (1-9).
        """
        if self.selected_cell and self.selected_cell.editable:
            self.selected_cell.set_sketched_value(value)

    def place_number(self):
        """
        Sets the cell's value to the sketched value, making it a permanent entry.
        """
        if self.selected_cell and self.selected_cell.editable:
            value = self.selected_cell.sketched_value
            if value != 0:
                self.selected_cell.set_cell_value(value)
                self.update_board()

    def clear(self):
        """
        Clears the value and sketched value of the selected cell.
        """
        if self.selected_cell and self.selected_cell.editable:
            self.selected_cell.set_cell_value(0)
            self.selected_cell.set_sketched_value(0)
            self.update_board()

    def reset_to_original(self):
        """
        Resets the board
        """
        for row in range(9):
            for col in range(9):
                cell = self.grid[row][col]
                if cell.editable:
                    cell.set_cell_value(0)
                    cell.set_sketched_value(0)
        self.update_board()

    def is_full(self):
        """
        Checks if the board is completely filled or not.

        Returns:
        - bool: True if all cells have a value other than 0, False otherwise.
        """
        for row in range(9):
            for col in range(9):
                if self.grid[row][col].value == 0:
                    return False
        return True

    def update_board(self):
        """
        Updates the internal board_values with the current cell values.
        """
        for row in range(9):
            for col in range(9):
                self.board_values[row][col] = self.grid[row][col].value

    def find_empty(self):
        """
        Finds an empty cell on the board.
            Tuple is much easier to return here than a list.

        Returns:
        - tuple: (row, col) of the first empty cell found.
        - None: If there are no empty cells.
        """
        for row in range(9):
            for col in range(9):
                if self.grid[row][col].value == 0:
                    return row, col
        return None

    def check_board(self):
        """
        Checks if current board state matches the solution.

        Returns:
        - bool: True if the board matches the solution, False otherwise.
        """
        for row in range(9):
            for col in range(9):
                if self.board_values[row][col] != self.solution[row][col]:
                    return False
        return True

    def move_selection(self, direction):
        """
        Moves the selected cell in the specified direction.

        Parameters:
        - direction (str): The direction to move ('up', 'down', 'left', 'right').
        """
        if self.selected_cell:
            row = self.selected_cell.row
            col = self.selected_cell.col
            if direction == 'up' and row > 0:
                row -= 1
            elif direction == 'down' and row < 8:
                row += 1
            elif direction == 'left' and col > 0:
                col -= 1
            elif direction == 'right' and col < 8:
                col += 1
            else:
                return
            self.select(row, col)