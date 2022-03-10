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
    Returns: Positions array which contains the positions that are not marked by either x or o
    """

    def availablePositions(self):
        positions = []
        for i in range(BOARD_ROWS):
            for j in range(BOARD_COLS):
                if board[i, j] == 0:
                    positions.append((i, j))  
        return positions


    """
    Marks the symbol on the board array

    Args: position -> Tuple of 2 numbers representing row and col values 

    """
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
        


    """
    humanPlayerAction is a method used for human input on the boad, after receiving play_order variable which represents either 1 or 2 depending on starting position
    it will declare p1 or p2 as a human player and ask for an input

    Args: play_order --> Number that represents either playing first or second( 1 or 2 )
    Returns : p_action --> tuple that represents chosen board position
    """
    def humanPlayerAction(self,play_order):
        if(play_order == 1):
            p1_action = self.p1.chooseAction()
            self.updateState(p1_action)
            return p1_action
        else:
            p2_action = self.p2.chooseAction()
            self.updateState(p2_action)
            return p2_action


    """
    Works same as a humanPlayerAction but Ai chooseAction requires more parametars like positons(array of spots taken on the board), board array and a playersmybol

    Args: play_order --> Number that represents either playing first or second( 1 or 2 )
    Returns : p_action --> tuple that represents chosen board position
    """
    def aiPlayerAction(self,play_order):
        positions = self.availablePositions()
        if(play_order == 1):
            p1_action = self.p1.chooseAction(positions, board, self.playerSymbol)
            self.updateState(p1_action)
            return p1_action
        else:
            p2_action = self.p2.chooseAction(positions, board, self.playerSymbol)
            self.updateState(p2_action)
            return p2_action

    """
    Method user for checking the board for a winner after every move and calling popup class for displaying it.
    Cheking for winner is done by winner() method defined above which returns 1/-1/None depending on the outcome

    Args: player --> Player names 
    Returns : 
    """
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
        

    """
    Used for separating/chosing gamemodes and assigning play orders

    GAMEMODES: 
            0- Player VS Player
            1- Player VS AI
            2- AI VS Player
    Args: gamemode --> int that represents our wanted gamemode
        
    """
    def play(self,gamemode):
        btn = GameScreen(app)
        if(gamemode == 0): 
            while not self.isEnd:
                action = self.humanPlayerAction(1)
                btn.changeButtonState(action)
                self.checkwin(self.p1.name)

                action = self.humanPlayerAction(2)
                btn.changeButtonState(action)
                self.checkwin(self.p2.name)
        elif(gamemode == 1):
            while not self.isEnd:
                action = self.humanPlayerAction(1)
                btn.changeButtonState(action)
                self.checkwin(self.p1.name)   

                action = self.aiPlayerAction(2)
                btn.changeButtonState(action)
                self.checkwin(self.p2.name)

        elif(gamemode == 2):
            while not self.isEnd:
                action = self.aiPlayerAction(1)
                btn.changeButtonState(action)
                self.checkwin(self.p1.name)

                action = self.humanPlayerAction(2)
                btn.changeButtonState(action)
                self.checkwin(self.p2.name)     


