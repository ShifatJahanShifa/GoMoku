import numpy as np
from gameBoard_final import GameBoard, BLACK, WHITE, EMPTY
from best_move_final import get_best_move


class GameRunner:
    def __init__(self, size=19, depth=2):
        self.size = size
        self.depth = depth
        self.difficulty_level = 'easy'  # Default level
        self.finished = False
        self.restart()

    def restart(self, player_index=-1, level='easy'):
        self.is_max_state = True if player_index == -1 else False
        self.state = GameBoard(self.size)
        self.difficulty_level = level
        self.ai_color = -player_index

    def play(self, i, j):
        position = (i, j)
        if self.state.color != self.ai_color:
            return False
        if not self.state.is_valid_position(position):
            return False
        self.state = self.state.next(position)
        self.finished = self.state.is_terminal()
        return True

    def aiplay(self):
        # import time
        # t = time.time()
        if self.state.color == self.ai_color:
            return False, (0, 0)
        move, value = get_best_move(self.state, self.depth, self.is_max_state, self.difficulty_level)
        self.state = self.state.next(move)
        self.finished = self.state.is_terminal()
        # print(time.time() - t)
        return True, move

    def get_status(self):
        board = self.state.values
        return {
            'board': board.tolist(),
            'next': -self.state.color,
            'finished': self.finished,
            'winner': self.state.winner,
            # 'debug_board': self.state.__str__()
        }
