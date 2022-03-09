from constants import *
import numpy as np
from popups import PopupMessage
from game_screen import GameScreen


class GameLogic:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.isEnd = False
        # init p1 plays first
        self.playerSymbol = 1

    #Checks winning conditions
    def winner(self):
        # Checking rows
        for i in range(BOARD_ROWS):
            if sum(board[i, :]) == 3:
                self.isEnd = True
                return 1
            if sum(board[i, :]) == -3:
                self.isEnd = True
                return -1
        # Checking columns
        for i in range(BOARD_COLS):
            if sum(board[:, i]) == 3:
                self.isEnd = True
                return 1
            if sum(board[:, i]) == -3:
                self.isEnd = True
                return -1
        # Checking diagonals
        diag_sum1 = sum([board[i, i] for i in range(BOARD_COLS)])
        diag_sum2 = sum([board[i, BOARD_COLS - i - 1] for i in range(BOARD_COLS)])
        diag_sum = max(abs(diag_sum1), abs(diag_sum2))
        if diag_sum == 3:
            self.isEnd = True
            if diag_sum1 == 3 or diag_sum2 == 3:
                return 1
            else:
                return -1

        # If there are no available positions its a tie
        if len(self.availablePositions()) == 0:
            self.isEnd = True
            return 0

        self.isEnd = False
        return None


    """
    Method that keeps track of free and taken spots on the board

    Args: None
    Returns: Positions array which contains the positions that are marked by either x or o
    """
    def availablePositions(self):
        positions = []
        for i in range(BOARD_ROWS):
            for j in range(BOARD_COLS):
                if board[i, j] == 0:
                    positions.append((i, j))  
        return positions


    def updateState(self, position):
        board[position] = self.playerSymbol
        # Switch to another player

        self.playerSymbol *= -1

    # Resets the board
    @staticmethod
    def reset():
        global board
        global playerSymbol
        global isEnd


        board = np.zeros((BOARD_ROWS, BOARD_COLS))
        isEnd = False
        playerSymbol = 1

    
    
    def humanPlayerAction(self,player):
        if(player == 1):
            p1_action = self.p1.chooseAction()
            self.updateState(p1_action)
            return p1_action
        else:
            p2_action = self.p2.chooseAction()
            self.updateState(p2_action)
            return p2_action

    def aiPlayerAction(self,player):
        positions = self.availablePositions()
        if(player == 1):
            p1_action = self.p1.chooseAction(positions, board, self.playerSymbol)
            self.updateState(p1_action)
            return p1_action
        else:
            p2_action = self.p2.chooseAction(positions, board, self.playerSymbol)
            self.updateState(p2_action)
            return p2_action

    def checkwin(self,player):
        win = self.winner()
        if win is not None:
            if win == 1:
                PopupMessage(app,player)
            elif win == -1:
                PopupMessage(app,player)
            else:
                PopupMessage(app,"Tie")
            self.reset()    
        

    def play(self,order):
        btn = GameScreen(app)
        if(order == 0): 
            while not self.isEnd:
                action = self.humanPlayerAction(1)
                btn.changeButtonState(action)
                self.checkwin(self.p1.name)

                action = self.humanPlayerAction(2)
                btn.changeButtonState(action)
                self.checkwin(self.p2.name)
        elif(order == 1):
            while not self.isEnd:
                action = self.humanPlayerAction(1)
                btn.changeButtonState(action)
                self.checkwin(self.p1.name)   

                action = self.aiPlayerAction(2)
                btn.changeButtonState(action)
                self.checkwin(self.p2.name)

        elif(order == 2):
            while not self.isEnd:
                action = self.aiPlayerAction(1)
                btn.changeButtonState(action)
                self.checkwin(self.p1.name)

                action = self.humanPlayerAction(2)
                btn.changeButtonState(action)
                self.checkwin(self.p2.name)     


        

        

