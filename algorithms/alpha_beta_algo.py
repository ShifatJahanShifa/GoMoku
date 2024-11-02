import math

def alpha_beta(state,alpha,beta,depth,is_max_state):

    if depth == 0 or state.is_terminal():
        return evaluation_state(state, -state.color)

    if is_max_state:
        best_value = -math.inf
        for move in state.legal_moves():
            value = alpha_beta(state.next(move),
                               alpha,
                               beta,
                               depth-1,
                               False)
            best_value = max(best_value,value)
            alpha = max(alpha,best_move)
            if beta <= alpha:
                break

        return best_value

    else:
        best_value = math.inf
        for move in state.legal_moves():
            value = minimax(state.next(move),
                            alpha,
                            beta,
                            depth-1,
                            True)
            best_move = min(best_value,value)
            beta=min(beta,best_value)
            if beta <= alpha:
                break
        return best_value

    