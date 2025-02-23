import pygame as pg
import graphics
import game_logic
import computer_player

# Initialize pygame
pg.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_HEIGHT = SCREEN_HEIGHT // 3
CELL_WIDTH = SCREEN_WIDTH // 3
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
game_board = [['-' for _ in range(3)] for _ in range(3)]

# Screen
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Initializations before game loop
screen.fill(WHITE)
graphics.draw_board(screen, BLACK, SCREEN_HEIGHT, SCREEN_WIDTH)
run = True
player1_turn = True
round = 0

# Game loop
while run:

    if round > 4:
        winner = game_logic.determine_if_player_won(game_board)
        if winner:
            print(f'Player {winner} won')
            run = False
        elif round == 9:
            print('Its a draw')
            run = False

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        
        elif event.type == pg.MOUSEBUTTONDOWN:
            round += 1
            (row, column) = game_logic.determine_what_cell_user_clicked(event.pos, CELL_HEIGHT, CELL_WIDTH)
            cell_is_free = game_logic.cell_is_empty(row, column, game_board)
            if player1_turn and cell_is_free:
                graphics.draw_x_in_the_cell_clicked(screen, BLACK, CELL_CENTER_POINTS[row, column])
                game_logic.mark_cell(row, column, 1, game_board)
                player1_turn = not player1_turn
            elif cell_is_free:
                graphics.draw_circle_in_the_cell_clicked(screen, RED, CELL_CENTER_POINTS[row, column])
                game_logic.mark_cell(row, column, 2, game_board)
                player1_turn = not player1_turn 

    pg.display.update()

pg.quit()
