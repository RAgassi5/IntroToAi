
def base_heuristic(curr_state):
    #add code here
    #simple heuristic: compare how many moves each player has
    moves_p1 = len(_potential_moves_for(curr_state, 1))
    moves_p2 = len(_potential_moves_for(curr_state, 2))

    return moves_p1 - moves_p2

def advanced_heuristic(curr_state):
    #count mobility
    p1_moves = _potential_moves_for(curr_state, 1)
    p2_moves = _potential_moves_for(curr_state, 2)

    mobility = len(p2_moves) - len(p1_moves)

    # basic distance measure between players (Manhattan)
    locs = curr_state.get_player_locations()
    p1 = locs[1]
    p2 = locs[2]
    distance = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    # check if a player is about to be stuck
    p1_future_trap = len(p1_moves) == 0
    p2_future_trap = len(p2_moves) == 0

    trap_bonus = 0
    if p2_future_trap:
        trap_bonus += 500  #player 1 is close to winning
    if p1_future_trap:
        trap_bonus -= 500  # player 1 is close to losing

    # Combine everything in to one score
    score = (3 * mobility + 0.2 * distance + trap_bonus)

    return score


def _potential_moves_for(curr_state, player_id):
    """
    compute possible knight moves for the given player
    """
    loc = curr_state.get_player_locations()[player_id]
    grid = curr_state.get_grid()
    moves = []

    for i in range(-2, 3):
        for j in range(-2, 3):
            #keep only legal knight-like possible moves
            if abs(i) == abs(j) or i == 0 or j == 0:
                continue
            new_pos = (loc[0] + i, loc[1] + j)
            if _is_legal_for(grid, new_pos):
                moves.append(new_pos)

    return moves


def _is_legal_for(grid, pos):
    """
    check if a square is inside the board and not visited yet
    """
    r, c = pos
    if r < 0 or r >= len(grid):
        return False
    if c < 0 or c >= len(grid[0]):
        return False
    return grid[pos] == 0
