import pygame as pg

pg.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_CENTER_POINTS = {(0, 0) : (SCREEN_WIDTH / 6, SCREEN_HEIGHT / 6),
                (1, 0) : (SCREEN_WIDTH / 6, SCREEN_HEIGHT / 2),
                (2, 0) : (SCREEN_WIDTH / 6, SCREEN_HEIGHT * (5 / 6)),
                (0, 1) : (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 6),
                (1, 1) : (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2),
                (2, 1) : (SCREEN_WIDTH / 2, SCREEN_HEIGHT * (5 / 6)),
                (0, 2) : (SCREEN_WIDTH * (5 / 6), SCREEN_HEIGHT / 6),
                (1, 2) : (SCREEN_WIDTH * (5 / 6), SCREEN_HEIGHT / 2),
                (2, 2) : (SCREEN_WIDTH * (5 / 6), SCREEN_HEIGHT * (5 / 6))
                }

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Screen
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(WHITE)

# Functions

def determine_what_cell_user_clicked(x: float, y: float) -> tuple[int, int]:
    cell_height = SCREEN_HEIGHT // 3
    cell_width = SCREEN_WIDTH // 3

    row = y // cell_height
    column = x // cell_width
    return (row, column)

def draw_circle_in_the_cell_player2_clicked(row: int, column: int):
    pg.draw.circle(screen, RED, CELL_CENTER_POINTS[(row, column)], 50, 5)

def draw_x_in_the_cell_player1_clicked(row: int, column: int):
    return 0

def draw_board():
    # Horizontal lines
    pg.draw.line(screen, BLACK, (0, SCREEN_HEIGHT // 3), (SCREEN_WIDTH, SCREEN_HEIGHT // 3), 5)
    pg.draw.line(screen, BLACK, (0, SCREEN_HEIGHT - (SCREEN_HEIGHT // 3)), (SCREEN_WIDTH,SCREEN_HEIGHT - (SCREEN_HEIGHT // 3)), 5) 
    # Vertical lines
    pg.draw.line(screen, BLACK, (SCREEN_WIDTH // 3, 0), (SCREEN_WIDTH // 3, SCREEN_HEIGHT), 5)
    pg.draw.line(screen, BLACK, (SCREEN_WIDTH - (SCREEN_WIDTH // 3), 0), (SCREEN_WIDTH - (SCREEN_WIDTH // 3), SCREEN_HEIGHT), 5)


run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    
    if event.type == pg.MOUSEBUTTONDOWN:
        mouse_pos = event.pos
        (row, column) = determine_what_cell_user_clicked(mouse_pos[0], mouse_pos[1])
        draw_circle_in_the_cell_player2_clicked(row, column)
    
    draw_board() 
    pg.display.flip()

pg.quit()