import game_logic

def find_all_empty_cells(current_game_board: list[list[str]]) -> list[tuple[int, int]]:
    empty_cells = []
    n = len(current_game_board)
    for row in range(n):
        for column in range(n):
            if current_game_board[row][column] == '-':
                empty_cells.append((row, column))

    return empty_cells

def miniMax(position: list[list[str]], round, maximizingPlayer: bool, alpha: float, beta: float, computer_player: int, player: int, move: tuple[int, int]) -> tuple[float, tuple[int, int]]:
    if round > 4:
        winner = game_logic.determine_if_player_won(position)
        if winner == computer_player:
            return (1.0, move)
        elif winner == player:
            return (-1.0, move)
        elif winner == 0 and round == 9: # Draw
            return (0.0, move)

    empty_cells = find_all_empty_cells(position)

    if maximizingPlayer:
        maxEval = -float('inf')
        best_move = move
        for row, column in empty_cells:
            position[row][column] = 'X' if computer_player == 1 else 'O'
            eval = miniMax(position, round + 1, not maximizingPlayer, alpha, beta, computer_player, player, (row, column))
            position[row][column] = '-'
            if eval[0] > maxEval:
                maxEval = eval[0]
                best_move = (row, column)
            alpha = max(alpha, eval[0])
            if beta <= alpha:
                break
        return (maxEval, best_move)

    else:
        minEval = float('inf')
        best_move = move
        for row, column in empty_cells:
            position[row][column] = 'O' if player == 2 else 'X'
            eval = miniMax(position, round + 1, not maximizingPlayer, alpha, beta, computer_player, player, (row, column))
            position[row][column] = '-'
            if eval[0] < minEval:
                minEval = eval[0]
                best_move = (row, column)
            beta = min(beta, eval[0])
            if beta <= alpha:
                break
        return (minEval, best_move)
