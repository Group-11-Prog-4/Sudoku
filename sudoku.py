import pygame
import sys
import sudoku_generator
import copy

pygame.init()

# Screen dimensions and window setup
screen_width, screen_height = 750, 800
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
    boards = sudoku_generator.generate_sudoku(9, removed)
    number_grid = boards[0]
    solved = boards[1]
    user_input_grid = [[False for _ in range(9)] for _ in range(9)]  # To track cells where user inputs numbers
    selected_cell = None
    og_grid = copy.deepcopy(number_grid)
    
    def reset_game():
        nonlocal number_grid
        # Reset the number grid to its initial state and clear user inputs
        number_grid = copy.deepcopy(og_grid)
        

    def draw_button(screen, text, x, y, width, height, color):
        button_font = pygame.font.SysFont('comicsansms', 20)
        pygame.draw.rect(screen, color, (x, y, width, height))
        text_surf = button_font.render(text, True, BLACK)
        text_rect = text_surf.get_rect(center=(x + (width / 2), y + (height / 2)))
        screen.blit(text_surf, text_rect)

    def draw_game_buttons():
        draw_button(screen, "Reset", 150, 750, 100, 30, BLUE)
        draw_button(screen, "Restart", 350, 750, 100, 30, BLUE)
        draw_button(screen, "Exit", 550, 750, 100, 30, BLUE)
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
        for i in range(9):
            for j in range(9):
                output = number_grid[i][j]
                if output != 0:
                    color = pygame.Color("gray") if user_input_grid[i][j] else pygame.Color("black")
                    text = font.render(str(output), True, color)
                    screen.blit(text, (j * 80 + 40, i * 80 + 40))
            # Highlight the selected cell
        if selected_cell:
            pygame.draw.rect(screen, pygame.Color("yellow"),
                             pygame.Rect(selected_cell[1] * 80 + 15, selected_cell[0] * 80 + 15, 80, 80), 5)
    
    
    def continue_game():
        
        for i in range(9):
            for j in range(9):
                if number_grid[i][j] == 0:
                    return True
        
        for i in range(9):
            for j in range(9):
                if number_grid[i][j] == solved[i][j]:
                    continue
                else:
                    display_game_over_screen()
                    pygame.display.update()
        display_game_won_screen()
        pygame.display.update()
        
                    

    game_in_progress = True
    while game_in_progress and continue_game():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Get mouse position and convert it to grid coordinates
                x, y = event.pos
                row, col = (y - 15) // 80, (x - 15) // 80
                if 0 <= row < 9 and 0 <= col < 9:
                    selected_cell = [row, col]
                    
                if 150 < x < 250 and 750 < y < 780:
                    print("reset")
                    reset_game()
                    pygame.display.update()
                elif 350 < x < 450 and 750 < y < 780:
                    game_start_screen()
                elif 550 < x < 650 and 750 < y < 780:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.KEYDOWN and event.key not in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                if selected_cell and event.unicode.isdigit():
                    number = int(event.unicode)
                    if number in range(1, 10):
                        if og_grid[selected_cell[0]][selected_cell[1]] != 0:
                            continue
                        else:
                            number_grid[selected_cell[0]][selected_cell[1]] = number
                            user_input_grid[selected_cell[0]][
                            selected_cell[1]] = True  # Mark this cell as having user input
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if selected_cell[0] > 0:
                        selected_cell[0] -= 1
                elif event.key == pygame.K_DOWN:
                    if selected_cell[0] < 8:
                        selected_cell[0] += 1
                elif event.key == pygame.K_LEFT:
                    if selected_cell[1] > 0:
                        selected_cell[1] -= 1
                elif event.key == pygame.K_RIGHT:
                    if selected_cell[1] < 8:
                        selected_cell[1] += 1

            draw_background()
            draw_numbers()
            draw_game_buttons()
            pygame.display.update()

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
