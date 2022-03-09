from constants import *
from player import Player
import pickle

class AiPlayer(Player):

    """
    chooseAction method 

    Args: positions --> array of available places on the board
          current_board --> array that represents current board state
          symbol --> char that represents current player
    Returns: action --> puts x or o on the board
    """

    def chooseAction(self, positions, current_board, symbol):
        value_max = -999

        for p in positions:
            next_board = current_board.copy()
            next_board[p] = symbol
            next_boardHash = self.getHash(next_board)
            value = 0 if self.states_value.get(next_boardHash) is None else self.states_value.get(next_boardHash)

            if value >= value_max:
                value_max = value
                action = p
            
        return action



