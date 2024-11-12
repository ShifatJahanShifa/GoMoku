# best_move.py

from gameBoard_final import GameBoard, BLACK, WHITE, EMPTY
import numpy as np
from minimax_alphaBeta_final import minimax
import math

# Import evaluation functions
from eval_fn1 import evaluation_state as eval_fn1
from eval_fn2 import evaluation_state as eval_fn2
from eval_fn3 import evaluation_state as eval_fn3

def get_best_move(state, depth, is_max_state, difficulty_level='easy'):
    # Select the appropriate evaluation function based on difficulty level
    if difficulty_level == 'easy':
        evaluation_function = eval_fn1
    elif difficulty_level == 'medium':
        evaluation_function = eval_fn2
    elif difficulty_level == 'hard':
        evaluation_function = eval_fn3
    else:
        raise ValueError("Unknown difficulty level")

    values = state.values
    best_value = -9999 if is_max_state else 9999
    best_move = (-1, -1)
    pieces = len(values[values != EMPTY])

    if pieces == 0:
        return first_move(state)
    if pieces == 1:
        return second_move(state)

    top_moves = get_top_moves(state, 10, is_max_state, evaluation_function)

    for move_n_value in top_moves:
        move = move_n_value[0]
        value = minimax(state.next(move), -10e5, 10e5, depth - 1, not is_max_state, evaluation_function)

        if ((is_max_state and value > best_value) or (not is_max_state and value < best_value)):
            best_value = value
            best_move = move

    if best_move[0] == -1 and best_move[1] == -1:
        return top_moves[0]

    return best_move, best_value

def get_top_moves(state, n, is_max_state, evaluation_function):
    color = state.color
    top_moves = []

    for move in state.legal_moves():
        evaluation = evaluation_function(state.next(move), color)
        top_moves.append((move, evaluation))
    return sorted(top_moves, key=lambda x: x[1], reverse=is_max_state)[:n]

def first_move(state):
    x = state.size // 2
    return np.random.choice((x - 1, x, x + 1), 2), 1


def second_move(state):
    i, j = state.last_move
    size = state.size
    i2 = i <= size // 2 and 1 or -1
    j2 = j <= size // 2 and 1 or -1
    return (i + i2, j + j2), 2
