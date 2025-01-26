import pygame as pg

pg.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Screen
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Cells
c1 = {'x1': 0, 'x2': SCREEN_WIDTH // 3, 'y1': 0, 'y2': SCREEN_HEIGHT // 3}
c2 = {}
c3 = []
c4 = []
c5 = []
c6 = []

def determine_what_cell_user_clicked(x, y):
    cell_height = SCREEN_HEIGHT // 3
    cell_width = SCREEN_WIDTH // 3

    row = y // cell_height
    column = x // cell_width
    return row, column

# Draw board
def draw_board():
    # Horizontal line
    pg.draw.line(screen, BLACK, (0, SCREEN_HEIGHT // 3), (SCREEN_WIDTH, SCREEN_HEIGHT // 3), 5)
    pg.draw.line(screen, BLACK, (0, SCREEN_HEIGHT - (SCREEN_HEIGHT // 3)), (SCREEN_WIDTH,SCREEN_HEIGHT - (SCREEN_HEIGHT // 3)), 5) 
    # Vertical line
    pg.draw.line(screen, BLACK, (SCREEN_WIDTH // 3, 0), (SCREEN_WIDTH // 3, SCREEN_HEIGHT), 5)
    pg.draw.line(screen, BLACK, (SCREEN_WIDTH - (SCREEN_WIDTH // 3), 0), (SCREEN_WIDTH - (SCREEN_WIDTH // 3), SCREEN_HEIGHT), 5)


run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    
    if event.type == pg.MOUSEBUTTONDOWN:
        mouse_pos = event.pos
        print(determine_what_cell_user_clicked(mouse_pos[0], mouse_pos[1]))
    
    screen.fill(WHITE)
    draw_board() 
    pg.display.flip()

pg.quit()