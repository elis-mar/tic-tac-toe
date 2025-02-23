import game_logic
from copy import deepcopy

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
        player_won = game_logic.determine_if_player_won(temp_game_board) if next_round > 4 else 0
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

def best_move() -> list[list[str]]:
    return [['']]

def minimax():
    return 0

