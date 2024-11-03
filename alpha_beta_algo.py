import math
#from gameBoard import legal_moves,next

from gameBoard import GameBoard, BLACK, WHITE, EMPTY

#import sys
#sys.path.append('./gameBoard.py')
#from .. import gameBoard
# In algorithms/alpha_beta_algo.py

from eval_fn import evaluation_state

BLACK = 1
WHITE = -1
EMPTY = 0
symbols = {BLACK: 'X', WHITE: 'O', EMPTY: '.'}

def alpha_beta(state,alpha,beta,depth,is_max_state):

    if depth == 0 or state.is_terminal():
        score = evaluation_state(state, -state.color)
        print(f"Evaluating state at depth {depth}: {score}")
        return score


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
            print(f"Max State - Move: {move}, Value: {value}, Best: {best_value}, Alpha: {alpha}, Beta: {beta}")

            if beta <= alpha:
                print("Pruning in Max State")
                break

        return best_value

    else:
        best_value = math.inf
        for move in state.legal_moves():
            value = alpha_beta(state.next(move),
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


def best_move(board, depth=3):
    best_one = -math.inf
    move_choice = None

    for move in board.legal_moves():
        new_board = board.next(move)
        eval = alpha_beta(new_board, depth, -math.inf, math.inf, False)
        if eval > best_one:
            best_one = eval
            move_choice = move

    return move_choice



if __name__ == "__main__":
    board_size = 10
    game_board = GameBoard(board_size)

    print("Initial Board:")
    print(game_board)

    moves = [(2, 2), (3, 3), (4, 4)]
    for move in moves:
        game_board[move] = BLACK  
        print(f"\nPlayer (BLACK) moved to {move}")
        print(game_board)

        ai_move = best_move(game_board)  # Corrected line
        if ai_move is not None:
            game_board[ai_move] = WHITE
            print(f"\nAI (WHITE) moved to {ai_move}")
            print(game_board)

        if game_board.is_terminal():
            winner = "BLACK" if game_board.winner == BLACK else "WHITE"
            print(f"Game over! Winner: {winner}")
            break