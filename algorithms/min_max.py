import math
from gameBoard import legal_moves,next

#import sys
#import source.utils as utils

def minimax(state, depth, is_max_state):

    if depth == 0 or state.is_terminal():
        return evaluation_state(state, -state.color)

    #if state.is_terminal() or d >= depth:
    #       return state.heuristic_value

    if is_max_state:
        best_value = -math.inf
        for move in state.legal_moves():
            value = minimax(state.next(move),
                            depth-1,
                            False)
            best_value=max(best_value,value)
        return best_value

    else:
        best_value = math.inf
        for move in state.legal_moves():
            value = minimax(state.next(move),
                            depth-1,
                            True)
            best_move = min(best_value,value)
        return best_value


