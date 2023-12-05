import pygame
import sys

pygame.init()

# Screen dimensions and window setup
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sudoku Game")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLUE = (55, 118, 171)
ORANGE = (255, 165, 0)


def draw_button(screen, text, x, y, width, height, color):
    """
    Function that draws a button. 
    Explanation of paramters: 
    Screen is the window where the buttons will be. 
    Text is the text displayed on the button. 
    x,y are the coordinates, width, height of the buttons. 
    """

    # To work with text in pygame, we create a font, render the image, and then blit the image to the screen. 
    button_font = pygame.font.SysFont('comicsansms', 20)
    pygame.draw.rect(screen, color, (x, y, width, height))
    text_surf = button_font.render(text, True, BLACK)
    text_rect = text_surf.get_rect(center=(x + (width / 2), y + (height / 2)))
    screen.blit(text_surf, text_rect)


def game_start_screen():
    """Create the menu display and handle button interactions based on event programming"""
    game_menu = True

    while game_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()

            if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if 150 < mouse_x < 250 and 350 < mouse_y < 400:
                        choose_easy()
                    elif 350 < mouse_x < 450 and 350 < mouse_y < 400:
                        choose_medium()
                    elif 550 < mouse_x < 650 and 350 < mouse_y < 400:
                        choose_hard()
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

def choose_easy():
    print("Easy chosen")
    # Add logic for starting the game with 'Easy' difficulty

def choose_medium():
    print("Medium chosen")
    # Add logic for starting the game with 'Medium' difficulty

def choose_hard():
    print("Hard chosen")
    # Add logic for starting the game with 'Hard' difficulty


def exit_game():
    """Exits the game."""
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    game_start_screen()
