import math
h = None


def alphabeta_max_h(current_game, _heuristic, depth=3, alpha = -math.inf, beta = math.inf):
    global h
    h = _heuristic
    # add code here
    #no available moves -> terminal
    if current_game.is_terminal():
        return current_game.get_score(), None

    #stop at depth limit and use heuristic
    if depth == 0:
        return h(current_game), None

    v = -math.inf
    best_move = None
    moves = current_game.get_moves()

    for move in moves:
        #evaluate next layer (Min player)
        score, _ = alphabeta_min_h(move, _heuristic, depth - 1, alpha, beta)

        #keep best score
        if score > v:
            v = score
            best_move = move

        #prune branch if possible
        if v >= beta:
            return v, None

        alpha = max(alpha, v)

    return v, best_move

def alphabeta_min_h(current_game, _heuristic, depth=3, alpha = -math.inf, beta = math.inf):
    global h
    h = _heuristic
    #no available moves -> terminal 
    if current_game.is_terminal():
        return current_game.get_score(), None

    # stop at depth limit and use heuristic
    if depth == 0:
        return h(current_game), None

    v = math.inf
    best_move = None
    moves = current_game.get_moves()

    for move in moves:
        #evaluate next layer (Max player)
        score, _ = alphabeta_max_h(move, _heuristic, depth - 1, alpha, beta)

        #keep lowest score
        if score < v:
            v = score
            best_move = move

        # prune branch if possible
        if v <= alpha:
            return v, None

        beta = min(beta, v)

    return v, best_move



def maximin(current_game, depth):
    global h
    if current_game.is_terminal():
        return current_game.get_score(), None
    if depth == 0:
        return h(current_game), None
    v = -math.inf
    moves = current_game.get_moves()
    for move in moves:
        mx, next_move = minimax(move, depth - 1)
        if v < mx:
            v = mx
            best_move = move
    return v, best_move


def minimax(current_game, depth):
    global h
    if current_game.is_terminal():
        return current_game.get_score(), None
    if depth == 0:
        return h(current_game), None
    v = math.inf
    moves = current_game.get_moves()
    for move in moves:
        mx, next_move = maximin(move, depth - 1)
        if v > mx:
            v = mx
            best_move = move

    return v, best_move
