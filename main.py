import pygame as pg

# Initialize pygame
pg.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_CENTER_POINTS = {
                    (0, 0) : (SCREEN_WIDTH / 6, SCREEN_HEIGHT / 6),
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

# Global variables
cells_marked_with_x = [[False for _ in range(3)] for _ in range(3)]
cells_marked_with_y = [[False for _ in range(3)] for _ in range(3)]

# Screen
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Functions for drawing game elements
def draw_circle_in_the_cell_clicked(row: int, column: int):
    pg.draw.circle(screen, RED, CELL_CENTER_POINTS[(row, column)], 50, 5)

def draw_x_in_the_cell_clicked(row: int, column: int):
    cell_center_pos = CELL_CENTER_POINTS[(row, column)]
    x = cell_center_pos[0]
    y = cell_center_pos[1]
    pg.draw.line(screen, BLACK, (x + 35, y - 35), (x - 35, y + 35), 5)
    pg.draw.line(screen, BLACK, (x + 35, y + 35), (x - 35, y - 35), 5)

def draw_board():
    # Horizontal lines
    pg.draw.line(screen, BLACK, (0, SCREEN_HEIGHT // 3), (SCREEN_WIDTH, SCREEN_HEIGHT // 3), 5)
    pg.draw.line(screen, BLACK, (0, SCREEN_HEIGHT - (SCREEN_HEIGHT // 3)), (SCREEN_WIDTH,SCREEN_HEIGHT - (SCREEN_HEIGHT // 3)), 5) 
    # Vertical lines
    pg.draw.line(screen, BLACK, (SCREEN_WIDTH // 3, 0), (SCREEN_WIDTH // 3, SCREEN_HEIGHT), 5)
    pg.draw.line(screen, BLACK, (SCREEN_WIDTH - (SCREEN_WIDTH // 3), 0), (SCREEN_WIDTH - (SCREEN_WIDTH // 3), SCREEN_HEIGHT), 5)

# Functions for game logic
def determine_what_cell_user_clicked(mouse_click_position: tuple[float, float]) -> tuple[int, int]:
    x = mouse_click_position[0]
    y = mouse_click_position[1]
    cell_height = SCREEN_HEIGHT // 3
    cell_width = SCREEN_WIDTH // 3
    row = y // cell_height
    column = x // cell_width
    return (row, column)

def check_if_cell_is_free(row: int, column: int):
    if cells_marked_with_x[row][column] or cells_marked_with_y[row][column]:
        return False
    return True

def mark_cell(row: int, column: int, player: int):
    if player == 1:
        cells_marked_with_x[row][column] = True
    else:
        cells_marked_with_y[row][column] = True 

# Initializations before game loop
screen.fill(WHITE)
draw_board() 
player1_turn = True
run = True

# Game loop
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        
        elif event.type == pg.MOUSEBUTTONDOWN:
            (row, column) = determine_what_cell_user_clicked(event.pos)
            cell_is_free = check_if_cell_is_free(row, column)
            if player1_turn and cell_is_free:
                draw_x_in_the_cell_clicked(row, column)
                mark_cell(row, column, 1)
                player1_turn = not player1_turn
            elif cell_is_free:
                draw_circle_in_the_cell_clicked(row, column)
                mark_cell(row, column, 2)
                player1_turn = not player1_turn 

    pg.display.flip()

pg.quit()