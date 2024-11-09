import math
#from gameBoard import legal_moves,next

from gameBoard import GameBoard, BLACK, WHITE, EMPTY

#import sys
#sys.path.append('./gameBoard.py')
#from .. import gameBoard
# In algorithms/alpha_beta_algo.py

from eval_fn import evaluation_state



def minimax(state,alpha,beta,depth,is_max_state):

    if depth == 0 or state.is_terminal():
        score = evaluation_state(state, -state.color)
        print(f"Evaluating state at depth {depth}: {score}")
        return score


    if is_max_state:
        best_value = -math.inf
        for move in state.legal_moves():
            value = minimax(state.next(move),
                               alpha,
                               beta,
                               depth-1,
                               False)
            best_value = max(best_value,value)

            alpha = max(alpha,best_move)
            print(f"Max State - Move: {move}, Value: {value}, Best: {best_value}, Alpha: {alpha}, Beta: {beta}")

            if beta <= alpha:
                print("Pruning in Max State")
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
            print(f"Min State - Move: {move}, Value: {value}, Best: {best_value}, Alpha: {alpha}, Beta: {beta}")

            if beta <= alpha:
                print("Pruning in Min State")
                break
        return best_value