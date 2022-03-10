from constants import *
import pickle

"""
Class Player is a parent class of HumanPlayer and AIPlayer

Used for defining player name, getting board hash and save/load policy
"""
class Player:
    def __init__(self, name):
        self.name = name
        self.states_value = {}  

    #Get unique hash for current board
    def getHash(self, board):
        boardHash = str(board.reshape(BOARD_COLS * BOARD_ROWS))
        return boardHash

    """
    Saves q learning policy, required during learning
    
    """
    def savePolicy(self):
        fw = open('policy_' + str(self.name), 'wb')
        pickle.dump(self.states_value, fw)
        fw.close()

    """
    Loads q learning policy, required for playing vs AIPlayer

    Args: file --> File name
    
    """
    def loadPolicy(self, file):
        fr = open(file, 'rb')
        self.states_value = pickle.load(fr)
        fr.close()