import pygame as pg

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
board = [[None for _ in range(3)] for _ in range(3)]

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
    row = y // CELL_HEIGHT
    column = x // CELL_WIDTH
    return (row, column)

def check_if_cell_is_free(row: int, column: int) -> bool: return board[row][column] == None

def mark_cell(row: int, column: int, player: int):
    if player == 1:
        board[row][column] = 'X'
    else:
        board[row][column] = 'O'

def all_marked_x(indexes: list[tuple]) -> bool: return all(board[r][c] == 'X' for (r, c) in indexes)

def all_marked_o(indexes: list[tuple]) -> bool: return all(board[r][c] == 'O' for (r, c) in indexes)

def determine_if_victory_in_column() -> int:
    for i in range(3):
        indexes = [(0, i), (1, i), (2, i)]
        if all_marked_x(indexes):
            return 1
        if all_marked_o(indexes):
            return 2
    return 0
    
def determine_if_victory_in_row() -> int:
    for i in range(3):
        indexes = [(i, 0), (i, 1), (i, 2)]
        if all_marked_x(indexes):
            return 1
        if all_marked_o(indexes):
            return 2
    return 0

def determine_if_victory_in_diagonal() -> int:
    diagonals = [
        [(i, i) for i in range(3)], 
        [(i, 2 - i) for i in range(3)]
    ]
    
    for diagonal in diagonals:
        if all_marked_x(diagonal):
            return 1
        if all_marked_o(diagonal):
            return 2
    return 0 

def determine_if_player_won():
    for determine_winner in (determine_if_victory_in_row, determine_if_victory_in_column, determine_if_victory_in_diagonal):
        winner = determine_winner()
        if winner:
            return winner
    return 0

# Functions for the computer player logic
game_tree = {}

def generate_game_tree():
    game_states =  (((None for _ in range(3)) for _ in range(3)))

    return 0

def minimax():
    return 0


# Initializations before game loop
screen.fill(WHITE)
draw_board()
run = True
player1_turn = True
round = 0

# Game loop
while run:

    if round > 4:
        winner = determine_if_player_won()
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

    pg.display.update()



pg.quit()