import pygame

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False
        self.sketched_value = 0

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        font = pygame.font.Font(None, 36)
        cell_size = 50
        cell_x = self.col * cell_size
        cell_y = self.row * cell_size

        pygame.draw.rect(self.screen, (255, 255, 255), (cell_x, cell_y, cell_size, cell_size))
        pygame.draw.lines(self.screen, (0, 0, 0), True, [(cell_x, cell_y), (cell_x + cell_size, cell_y),
                                                         (cell_x + cell_size, cell_y + cell_size),
                                                         (cell_x, cell_y + cell_size)], 2)

        if self.selected:
            pygame.draw.rect(self.screen, (255, 0, 0), (cell_x, cell_y, cell_size, cell_size), 2)

        if self.value != 0:
            text = font.render(str(self.value), True, (0, 0, 0))
            self.screen.blit(text, (cell_x + 20, cell_y + 15))
        elif self.sketched_value != 0:
            text = font.render(str(self.sketched_value), True, (128, 128, 128))
            self.screen.blit(text, (cell_x + 5, cell_y + 5))


class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cells = [[Cell(0, row, col, screen) for col in range(width)] for row in range(height)]
        self.selected_cell = None

    def draw(self):
        cell_size = 50

        for row in range(self.height):
            for col in range(self.width):
                self.cells[row][col].draw()

                if (col + 1) % 3 == 0 and col + 1 != self.width:
                    pygame.draw.line(self.screen, (0, 0, 0), ((col + 1) * cell_size, row * cell_size),
                                     ((col + 1) * cell_size, (row + 1) * cell_size), 2)

            if (row + 1) % 3 == 0 and row + 1 != self.height:
                pygame.draw.line(self.screen, (0, 0, 0), (0, (row + 1) * cell_size),
                                 (self.width * cell_size, (row + 1) * cell_size), 2)

    def select(self, row, col):
        if self.selected_cell:
            self.selected_cell.selected = False

        self.selected_cell = self.cells[row][col]
        self.selected_cell.selected = True

    def click(self, x, y):
        cell_size = 50
        col = x // cell_size
        row = y // cell_size

        if 0 <= row < self.height and 0 <= col < self.width:
            return row, col
        else:
            return None

    def clear(self):
        if self.selected_cell:
            self.selected_cell.set_cell_value(0)

    def sketch(self, value):
        if self.selected_cell:
            self.selected_cell.set_sketched_value(value)

    def place_number(self, value):
        if self.selected_cell:
            self.selected_cell.set_cell_value(value)

    def reset_to_original(self):
        for row in range(self.height):
            for col in range(self.width):
                # Replace 0 with the original value if available, otherwise set to 0
                self.cells[row][col].value = 0  # Replace with actual original values

    def is_full(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.cells[row][col].value == 0:
                    return False
        return True

    def update_board(self):
        # Update the underlying 2D board with the values in all cells
        pass  # Add implementation if necessary

    def find_empty(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.cells[row][col].value == 0:
                    return row, col
        return None

    def check_board(self):
        # Check whether the Sudoku board is solved correctly
        pass  # Add implementation if necessary
