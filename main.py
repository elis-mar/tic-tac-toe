import pygame as pg
from copy import deepcopy

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

# Functions for drawing game elements

def draw_circle_in_the_cell_clicked(row: int, column: int) -> None:
    pg.draw.circle(screen, RED, CELL_CENTER_POINTS[(row, column)], 50, 5)

def draw_x_in_the_cell_clicked(row: int, column: int) -> None:
    cell_center_pos = CELL_CENTER_POINTS[(row, column)]
    x = cell_center_pos[0]
    y = cell_center_pos[1]
    pg.draw.line(screen, BLACK, (x + 35, y - 35), (x - 35, y + 35), 5)
    pg.draw.line(screen, BLACK, (x + 35, y + 35), (x - 35, y - 35), 5)

def draw_board() -> None:
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

def check_if_cell_is_free(row: int, column: int, board: list[list[str]]) -> bool: return board[row][column] == '-'

def mark_cell(row: int, column: int, player: int) -> None:
    if player == 1:
        game_board[row][column] = 'X'
    else:
        game_board[row][column] = 'O'

def all_marked_x(indexes: list[tuple], board: list[list[str]]) -> bool: return all(board[r][c] == 'X' for (r, c) in indexes)

def all_marked_o(indexes: list[tuple], board: list[list[str]]) -> bool: return all(board[r][c] == 'O' for (r, c) in indexes)

def determine_if_victory_in_column(board: list[list[str]]) -> int:
    for i in range(3):
        indexes = [(0, i), (1, i), (2, i)]
        if all_marked_x(indexes, board):
            return 1
        if all_marked_o(indexes, board):
            return 2
    return 0
    
def determine_if_victory_in_row(board: list[list[str]]) -> int:
    for i in range(3):
        indexes = [(i, 0), (i, 1), (i, 2)]
        if all_marked_x(indexes, board):
            return 1
        if all_marked_o(indexes, board):
            return 2
    return 0

def determine_if_victory_in_diagonal(board: list[list[str]]) -> int:
    diagonals = [
        [(i, i) for i in range(3)], 
        [(i, 2 - i) for i in range(3)]
    ]
    
    for diagonal in diagonals:
        if all_marked_x(diagonal, board):
            return 1
        if all_marked_o(diagonal, board):
            return 2
    return 0 

def determine_if_player_won(board: list[list[str]]) -> int:
    for determine_winner in (determine_if_victory_in_row, determine_if_victory_in_column, determine_if_victory_in_diagonal):
        winner = determine_winner(board)
        if winner:
            return winner
    return 0

# Functions and global variables for the computer player logic

def find_all_empty_cells(current_game_board: list[list[str]]) -> list[tuple[int, int]]:
    empty_cells = []
    n = len(current_game_board)
    for row in range(n):
        for column in range(n):
            if current_game_board[row][column] == '-':
                empty_cells.append((row, column))

    return empty_cells

# game_state: (0: board, 1: player1_turn, 2: player_won, 3: round)
def generate_game_states(current_game_state: tuple[list[list[str]], bool, int, int], empty_cells: list[tuple[int, int]]) -> list[tuple[list[list[str]], bool, int]]:
    game_states = []
    player1_turn = current_game_state[1]
    next_round = current_game_state[3] + 1
    for row, column in empty_cells:
        temp_game_board = deepcopy(current_game_state[0])
        temp_game_board[row][column] = 'X' if player1_turn else 'O'
        player_won = determine_if_player_won(temp_game_board) if next_round > 4 else 0
        game_states.append((temp_game_board, not player1_turn, player_won, next_round))
    return game_states

def board_to_int(game_board: list[list[str]]) -> int:
    mapping = {'-': 0b00, 'X': 0b01, 'O': 0b10}
    num = 0
    for row in game_board:
        for cell in row:
            num = (num << 2) | mapping[cell]
    return num

def generate_game_tree() -> dict[int, dict]:
    game_tree = {}
    stack = []
    # game_state: (0: board, 1: player1_turn, 2: player_won, 3: round)
    inital_game_state = ([['-' for _ in range(3)] for _ in range(3)], True, 0, 0) 
    stack.append(inital_game_state)

    while stack: 
        current_game_state = stack.pop()
        current_game_board = current_game_state[0]
        player_won_in_current_state = current_game_state[2] 
        current_game_round = current_game_state[3]
        key = board_to_int(current_game_board)

        if key not in game_tree:
             game_tree[key] = {
                'state': current_game_state,
                'next_states': []
            }

        if player_won_in_current_state or current_game_round == 9:
            continue

        else:
            empty_cells = find_all_empty_cells(current_game_board)
            new_game_states = generate_game_states(current_game_state, empty_cells)
   
            for new_game_state in new_game_states:
                new_key = board_to_int(new_game_state[0])

                if new_key not in game_tree:
                    game_tree[new_key] = {
                        'state': new_game_state,
                        'next_states': []
                    }

                game_tree[key]['next_states'].append(new_key)
                stack.append(new_game_state)

    return game_tree

game_tree = generate_game_tree()

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
        winner = determine_if_player_won(game_board)
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
            cell_is_free = check_if_cell_is_free(row, column, game_board)
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