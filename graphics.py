from pygame import draw

CIRCLE_RADIUS = 50
X_LINE_LENGTH = 35
LINE_THICKNESS = 5

def draw_circle_in_the_cell_clicked(screen, color: tuple[int, int, int], center: tuple[float, float]) -> None:
    draw.circle(screen, color, center, CIRCLE_RADIUS, LINE_THICKNESS)

def draw_x_in_the_cell_clicked(screen, color: tuple[int, int, int], center: tuple[float, float]) -> None:
    x, y = center
    draw.line(screen, color, (x + X_LINE_LENGTH, y - X_LINE_LENGTH), (x - X_LINE_LENGTH, y + X_LINE_LENGTH), LINE_THICKNESS)
    draw.line(screen, color, (x + X_LINE_LENGTH, y + X_LINE_LENGTH), (x - X_LINE_LENGTH, y - X_LINE_LENGTH), LINE_THICKNESS)

def draw_board(screen, color: tuple[int, int, int], screen_height: int, screen_width: int) -> None:
    # Horizontal lines
    draw.line(screen, color, (0, screen_height // 3), (screen_width, screen_height // 3), LINE_THICKNESS)
    draw.line(screen, color, (0, screen_height - (screen_height // 3)), (screen_width,screen_height - (screen_height // 3)), LINE_THICKNESS) 
    # Vertical lines
    draw.line(screen, color, (screen_width // 3, 0), (screen_width // 3, screen_height), LINE_THICKNESS)
    draw.line(screen, color, (screen_width - (screen_width // 3), 0), (screen_width - (screen_width // 3), screen_height), LINE_THICKNESS)

