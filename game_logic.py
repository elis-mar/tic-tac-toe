def determine_what_cell_user_clicked(mouse_click_position: tuple[float, float], cell_height: int, cell_width: int) -> tuple[int, int]:
    x, y = mouse_click_position
    row = int(y // cell_height)
    column = int(x // cell_width)
    return (row, column)

def cell_is_empty(row: int, column: int, board: list[list[str]]) -> bool: return board[row][column] == '-'

def mark_cell(row: int, column: int, player: int, game_board: list[list[str]]) -> None:
    game_board[row][column] = 'X' if player == 1 else 'O'

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
