import pygame 
import sys
import sudoku_generator

# Grid with grid vals put in

number_grid = sudoku_generator.generate_sudoku(9, 30)

pygame.init()
screen_size = 750, 750
screen = pygame.display.set_mode(screen_size)
font = pygame.font.SysFont(None, 60)

# Draws grid
def draw_background():
    screen.fill(pygame.Color("white"))
    pygame.draw.rect(screen, pygame.Color("red"), pygame.Rect(15, 15, 720, 720), 10)
    i = 1
    while (i * 80) < 720:
        lw = 5 if i % 3 > 0 else 10
        pygame.draw.line(screen, pygame.Color("red"), pygame.Vector2((i * 80)+ 15, 15), pygame.Vector2((i * 80) + 15, 735), lw)
        pygame.draw.line(screen, pygame.Color("red"), pygame.Vector2(15, (i * 80)+ 15), pygame.Vector2(735, (i * 80) + 15), lw)
        i += 1 

# Puts numbers in grid from sudoku_generator
def draw_numbers():
    row = 0
    offset = 40
    for i in range(9):
        for j in range(9):
            output = number_grid [i] [j]
            if output == 0:
                continue
            text = font.render(str(output), True, pygame.Color("black"))
            screen.blit(text, pygame.Vector2((j * 80) + offset + 5, (i * 80) + offset - 5))

def game_loop():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    draw_background()
    draw_numbers()
    pygame.display.flip()

def main():
    draw_background()

while 1:
    game_loop()
    

    