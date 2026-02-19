import math


def alphabeta_max(current_game, alpha = -math.inf, beta = math.inf):
    #add code here for alpha-beta
    if current_game.is_terminal():
        return current_game.get_score(), None

    v = -math.inf
    best_move = None
    moves = current_game.get_moves()
    for move in moves:
        score, _ = alphabeta_min(move, alpha, beta)

        if score > v:
            v = score
            best_move = move
        if v >= beta:
            return v, None

        alpha = max(alpha, v)

    return v, best_move

def alphabeta_min(current_game, alpha = -math.inf, beta = math.inf):
    #add code here for alpha-beta
    if current_game.is_terminal():
        return current_game.get_score(), None

    v = math.inf
    best_move = None
    moves = current_game.get_moves()
    for move in moves:
        score, _ = alphabeta_max(move, alpha, beta)

        if score < v:
            v = score
            best_move = move
        if v <= alpha:
            return v, None

        beta = min(beta, v)

    return v, best_move



def maximin(current_game):
    # add code here for alpha-beta algorithm
    if current_game.is_terminal():
        return current_game.get_score(), None
    v = -math.inf
    moves = current_game.get_moves()
    for move in moves:
        mx, next_move = minimax(move)
        if v < mx:
            v = mx
            best_move = move
    return v, best_move


def minimax(current_game):
    # add code here for alpha-beta algorithm
    if current_game.is_terminal():
        return current_game.get_score(), None
    v = math.inf
    moves = current_game.get_moves()
    for move in moves:
        mx, next_move = maximin(move)
        if v > mx:
            v = mx
            best_move = move
    return v, best_move
