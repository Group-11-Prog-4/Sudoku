import pygame
import sys
import sudoku_generator
#from sudokuu import game_loop
#from game_won_screen import display_game_won_screen
#from game_over_screen import display_game_over_screen

pygame.init()

# Screen dimensions and window setup
screen_width, screen_height = 800, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sudoku Game")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLUE = (55, 118, 171)
ORANGE = (255, 165, 0)

#Game States
MENU = 0
GAME_IN_PROGRESS = 1
GAME_OVER = 2
GAME_WON = 3

def main():
    running = True
    current_state = MENU

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if current_state == MENU:
            game_start_screen()
        elif current_state == GAME_IN_PROGRESS:
            game_loop()
        elif current_state == GAME_OVER:
            display_game_over_screen()
        elif current_state == GAME_WON:
            display_game_won_screen()

        pygame.display.update()


def game_start_screen():
    """Create the menu display and handle button interactions based on event programming."""

    def draw_button(screen, text, x, y, width, height, color):
        """
        Function that draws a button.
        Explanation of parameters:
        Screen is the window where the buttons will be.
        Text is the text displayed on the button.
        x, y are the coordinates, width, height of the buttons.
        """
        button_font = pygame.font.SysFont('comicsansms', 20)
        pygame.draw.rect(screen, color, (x, y, width, height))
        text_surf = button_font.render(text, True, BLACK)
        text_rect = text_surf.get_rect(center=(x + (width / 2), y + (height / 2)))
        screen.blit(text_surf, text_rect)

    game_menu = True
    while game_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if 150 < mouse_x < 250 and 350 < mouse_y < 400:
                    game_loop(30)
                elif 350 < mouse_x < 450 and 350 < mouse_y < 400:
                    game_loop(40)
                elif 550 < mouse_x < 650 and 350 < mouse_y < 400:
                    game_loop(50)
                elif 350 < mouse_x < 450 and 450 < mouse_y < 500:
                    exit_game()

        screen.fill(GRAY)  # Fill the background

        # Draw the "Welcome to Sudoku" message
        welcome_font = pygame.font.SysFont('comicsansms', 60)
        welcome_text = welcome_font.render("Welcome to Sudoku!", True, BLACK)
        welcome_rect = welcome_text.get_rect(center=(screen_width / 2, screen_height / 4))
        screen.blit(welcome_text, welcome_rect)

        difficulty_font = pygame.font.SysFont('comicsansms', 50)
        difficulty_text = difficulty_font.render("Choose a difficulty:", True, BLACK)
        difficulty_rect = difficulty_text.get_rect(center=(screen_width / 2, screen_height / 4 + 100))
        screen.blit(difficulty_text, difficulty_rect)

        # Draw buttons
        draw_button(screen, "Easy", 150, 350, 100, 50, BLUE)
        draw_button(screen, "Medium", 350, 350, 100, 50, BLUE)
        draw_button(screen, "Hard", 550, 350, 100, 50, BLUE)
        draw_button(screen, "Exit", 350, 450, 100, 50, BLUE)
        pygame.display.update()

def game_loop(removed):
    font = pygame.font.SysFont(None, 60)
    number_grid = sudoku_generator.generate_sudoku(9, removed)
    # Draws grid
    def draw_background():
        screen.fill(pygame.Color("white"))
        pygame.draw.rect(screen, pygame.Color("red"), pygame.Rect(15, 15, 720, 720), 10)
        i = 1
        while (i * 80) < 720:
            lw = 5 if i % 3 > 0 else 10
            pygame.draw.line(screen, pygame.Color("red"), pygame.Vector2((i * 80) + 15, 15),
                             pygame.Vector2((i * 80) + 15, 735), lw)
            pygame.draw.line(screen, pygame.Color("red"), pygame.Vector2(15, (i * 80) + 15),
                             pygame.Vector2(735, (i * 80) + 15), lw)
            i += 1

            # Puts numbers in grid from sudoku_generator

    def draw_numbers():
        row = 0
        offset = 40
        for i in range(9):
            for j in range(9):
                output = number_grid[i][j]
                if output == 0:
                    continue
                text = font.render(str(output), True, pygame.Color("black"))
                screen.blit(text, pygame.Vector2((j * 80) + offset + 5, (i * 80) + offset - 5))

    game_in_progress = True
    while game_in_progress:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            else:
                draw_background()
                draw_numbers()
                pygame.display.flip()

def display_game_won_screen():

    # Define colors
    BLACK = (0, 0, 0)
    GRAY = (200, 200, 200)
    BLUE = (55, 118, 171)

    def draw_button(screen, text, x, y, width, height, color):
        button_font = pygame.font.SysFont('comicsansms', 20)
        pygame.draw.rect(screen, color, (x, y, width, height))
        text_surf = button_font.render(text, True, BLACK)
        text_rect = text_surf.get_rect(center=(x + (width / 2), y + (height / 2)))
        screen.blit(text_surf, text_rect)

    def exit_game():
        pygame.quit()
        sys.exit()

    # Game Won Screen Logic
    game_menu = True
    while game_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if 325 < mouse_x < 425 and 350 < mouse_y < 400:
                    exit_game()

        screen.fill(GRAY)
        welcome_font = pygame.font.SysFont('comicsansms', 60)
        welcome_text = welcome_font.render("Game Won!", True, BLACK)
        welcome_rect = welcome_text.get_rect(center=(screen_width / 2, screen_height / 4))
        screen.blit(welcome_text, welcome_rect)
        draw_button(screen, "Exit", 325, 350, 100, 50, BLUE)
        pygame.display.update()

def display_game_over_screen():

    def draw_button(screen, text, x, y, width, height, color):
        button_font = pygame.font.SysFont('comicsansms', 20)
        pygame.draw.rect(screen, color, (x, y, width, height))
        text_surf = button_font.render(text, True, BLACK)
        text_rect = text_surf.get_rect(center=(x + (width / 2), y + (height / 2)))
        screen.blit(text_surf, text_rect)

    def exit_game():
        """Exits the game."""
        pygame.quit()
        sys.exit()

    # Game Over Screen Logic
    game_menu = True
    while game_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if 325 < mouse_x < 425 and 350 < mouse_y < 400:
                    game_start_screen()

        screen.fill(GRAY)
        welcome_font = pygame.font.SysFont('comicsansms', 60)
        welcome_text = welcome_font.render("Game Over :(", True, BLACK)
        welcome_rect = welcome_text.get_rect(center=(screen_width / 2, screen_height / 4))
        screen.blit(welcome_text, welcome_rect)
        draw_button(screen, "Restart", 325, 350, 100, 50, BLUE)
        pygame.display.update()


def exit_game():
    """Exits the game."""
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
