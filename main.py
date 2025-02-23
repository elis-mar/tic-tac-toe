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

# Screen
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Tic-Tac-Toe")

# Functions for menu screens and game loop
def main_menu() -> bool:
    graphics.clear_screen(screen)
    graphics.draw_main_menu(screen, SCREEN_WIDTH)
    pg.display.update()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                _, y = event.pos
                if 250 <= y <= 300:  # Play as X
                    return True # Player 1 turn
                elif 350 <= y <= 400:  # Play as O
                    return False # Player 2 turn


def play_game(player1_turn: bool) -> int:
    game_board = [['-' for _ in range(3)] for _ in range(3)]
    graphics.clear_screen(screen)
    graphics.draw_board(screen, SCREEN_HEIGHT, SCREEN_WIDTH)
    round_count = 0

    while True:
        if round_count > 4:
            winner = game_logic.determine_if_player_won(game_board)
            if winner:
                return winner
            elif round_count == 9:
                return 0

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                row, col = game_logic.determine_what_cell_user_clicked(event.pos, CELL_HEIGHT, CELL_WIDTH)
                if game_logic.cell_is_empty(row, col, game_board):
                    if player1_turn:
                        graphics.draw_x_in_the_cell_clicked(screen, CELL_CENTER_POINTS[row, col])
                        game_logic.mark_cell(row, col, 1, game_board)
                    else:
                        graphics.draw_circle_in_the_cell_clicked(screen, CELL_CENTER_POINTS[row, col])
                        game_logic.mark_cell(row, col, 2, game_board)

                    player1_turn = not player1_turn
                    round_count += 1

        pg.display.update()

def play_again_screen(winner: int) -> bool:
    graphics.clear_screen(screen)
    graphics.draw_play_again_menu(screen, winner, SCREEN_WIDTH)
    pg.display.update()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                _, y = event.pos
                if 300 <= y <= 350:  # Clicked "Yes"
                    return True
                elif 400 <= y <= 450:  # Clicked "No"
                    return False


def main():
    while True:
        player1_turn = main_menu()
        winner = play_game(player1_turn)

        if not play_again_screen(winner):
            break

    pg.quit()

if __name__ == "__main__":
    main()
