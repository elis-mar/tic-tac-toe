from pygame import draw, font

WHITE, BLACK, RED = (255, 255, 255), (0, 0, 0), (255, 0, 0)
CIRCLE_RADIUS = 50
X_LINE_LENGTH = 35
LINE_THICKNESS = 5

def draw_circle_in_the_cell_clicked(screen, center: tuple[float, float]) -> None:
    draw.circle(screen, RED, center, CIRCLE_RADIUS, LINE_THICKNESS)

def draw_x_in_the_cell_clicked(screen, center: tuple[float, float]) -> None:
    x, y = center
    draw.line(screen, BLACK, (x + X_LINE_LENGTH, y - X_LINE_LENGTH), (x - X_LINE_LENGTH, y + X_LINE_LENGTH), LINE_THICKNESS)
    draw.line(screen, BLACK, (x + X_LINE_LENGTH, y + X_LINE_LENGTH), (x - X_LINE_LENGTH, y - X_LINE_LENGTH), LINE_THICKNESS)

def draw_board(screen, screen_height: int, screen_width: int) -> None:
    # Horizontal lines
    draw.line(screen, BLACK, (0, screen_height // 3), (screen_width, screen_height // 3), LINE_THICKNESS)
    draw.line(screen, BLACK, (0, screen_height - (screen_height // 3)), (screen_width,screen_height - (screen_height // 3)), LINE_THICKNESS) 
    # Vertical lines
    draw.line(screen, BLACK, (screen_width // 3, 0), (screen_width // 3, screen_height), LINE_THICKNESS)
    draw.line(screen, BLACK, (screen_width - (screen_width // 3), 0), (screen_width - (screen_width // 3), screen_height), LINE_THICKNESS)

def draw_play_again_menu(screen, winner: int, screen_width: int) -> None:
    screen.fill(WHITE)
    text_style = font.Font(None, 50)

    if winner == 1:
        result_text = text_style.render("Player X (1) Won!", True, BLACK)
    elif winner == 2:
        result_text = text_style.render("Player O (2) Won!", True, BLACK)
    else:
        result_text = text_style.render("It's a Draw!", True, BLACK)

    again_text = text_style.render("Play Again?", True, BLACK)
    yes_text = text_style.render("Yes", True, BLACK)
    no_text = text_style.render("No", True, BLACK)

    # Position text
    screen.blit(result_text, (screen_width // 2 - 150, 100))
    screen.blit(again_text, (screen_width // 2 - 100, 200))
    screen.blit(yes_text, (screen_width // 2 - 50, 300))
    screen.blit(no_text, (screen_width // 2 - 50, 400))

def draw_main_menu(screen, screen_width: int) -> None:
    text_style = font.Font(None, 50)

    title_text = text_style.render("Tic-Tac-Toe", True, BLACK)
    play_x_text = text_style.render("Play as X (Player 1)", True, BLACK)
    play_o_text = text_style.render("Play as O (Player 2)", True, BLACK)

    screen.blit(title_text, (screen_width // 2 - 100, 100))
    screen.blit(play_x_text, (screen_width // 2 - 150, 250))
    screen.blit(play_o_text, (screen_width // 2 - 150, 350))

def clear_screen(screen) -> None:
    screen.fill(WHITE)
