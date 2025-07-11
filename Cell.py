import pygame


class Cell:
    def __init__(self, value, row, col, screen):
        """
        Cell class constructor

        Parameters:
        - value (int): The initial value of the cell (0 if empty).
        - row (int): The row index of the cell (0-8).
        - col (int): The column index of the cell (0-8).
        - screen (pygame.Surface): The Pygame screen where the cell will be drawn.
        """
        self.value = value
        self.sketched_value = 0
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False
        self.font = pygame.font.SysFont('arial', 40)  # If someone wants to change this font, they can
        self.sketch_font = pygame.font.SysFont('arial', 40)  # If someone wants to change this font, they can
        self.editable = self.value == 0

    def set_cell_value(self, value):
        """
        Sets the cell's value.

        Parameters:
        - value (int): The value to set in the cell.
        """
        self.value = value
        self.sketched_value = 0

    def set_sketched_value(self, value):
        """
        Sets the cell's sketched value.

        Parameters:
        - value (int): The sketched value to set in the cell.
        """
        self.sketched_value = value

    def draw(self):
        """
        Draws the cell and its value on the screen.

        If the cell has a nonzero value, that value is displayed.
        Otherwise, no value is displayed in the cell.
        The cell is outlined red if it is currently selected.
        """
        cell_size = 60
        x = self.col * cell_size
        y = self.row * cell_size

        # Cell background
        pygame.draw.rect(self.screen, pygame.Color('white'), (x, y, cell_size, cell_size))

        # Cell border
        if self.selected:
            pygame.draw.rect(self.screen, pygame.Color('red'), (x, y, cell_size, cell_size), 3)
        else:
            pygame.draw.rect(self.screen, pygame.Color('black'), (x, y, cell_size, cell_size), 1)

        # Draw the value if the cell is not empty
        if self.value != 0:
            # Center the cell value
            text = self.font.render(str(self.value), True, pygame.Color('black'))
            text_rect = text.get_rect(center=(x + cell_size / 2, y + cell_size / 2))
            self.screen.blit(text, text_rect)
        # Draw the sketched value if there is no final value
        elif self.sketched_value != 0:
            # Render sketched value in the top-left corner
            text = self.sketch_font.render(str(self.sketched_value), True, pygame.Color('gray'))
            self.screen.blit(text, (x + 5, y + 5))