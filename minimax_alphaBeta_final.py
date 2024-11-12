import math
from gameBoard_final import GameBoard, BLACK, WHITE, EMPTY
#from eval_fn1 import evaluation_state
    

def minimax(state,alpha,beta,depth,is_max_state, evaluation_function):

    if depth == 0 or state.is_terminal():
        score = evaluation_function(state, -state.color)
        print(f"Evaluating state at depth {depth}: {score}")
        return score


    if is_max_state:
        best_value = -9999
        for move in state.legal_moves():
            value = minimax(state.next(move),
                               alpha,
                               beta,
                               depth-1,
                               False, evaluation_function)
            best_value = max(best_value,value)

            alpha = max(alpha,best_move)
            print(f"Max State - Move: {move}, Value: {value}, Best: {best_value}, Alpha: {alpha}, Beta: {beta}")

            if beta <= alpha:
                print("Pruning in Max State")
                break

        return best_value

    else:
        best_value = 9999
        for move in state.legal_moves():
            value = minimax(state.next(move),
                            alpha,
                            beta,
                            depth-1,
                            True, evaluation_function)
            best_value= min(best_value,value)
            beta=min(beta,best_value)
            print(f"Min State - Move: {move}, Value: {value}, Best: {best_value}, Alpha: {alpha}, Beta: {beta}")

            if beta <= alpha:
                print("Pruning in Min State")
                break
        return best_value
