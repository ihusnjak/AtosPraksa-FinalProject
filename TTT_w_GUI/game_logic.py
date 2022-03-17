import constants
import global_variables
import numpy as np
from popups import PopupMessage
from game_screen import GameScreen
import requests

class GameLogic:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.isEnd = False
        self.board = np.zeros((constants.BOARD_ROWS, constants.BOARD_COLS))
        # init p1 plays first
        self.playerSymbol = 1
        self.counter = 0

    """
    Method that checks for winning conditions

    Args: 
    Returns: -1, 1, 0 or None
            None --> No winning conditions and no ties
            -1,1 --> Winning condition for one of the playersmybols
            0 --> Tie
    """
    def winner(self):
        # Checking rows
        for i in range(constants.BOARD_ROWS):
            if sum(self.board[i, :]) == 3:
                self.isEnd = True
                return 1
            if sum(self.board[i, :]) == -3:
                self.isEnd = True
                return -1
        # Checking columns
        for i in range(constants.BOARD_COLS):
            if sum(self.board[:, i]) == 3:
                self.isEnd = True
                return 1
            if sum(self.board[:, i]) == -3:
                self.isEnd = True
                return -1
        # Checking diagonals
        diag_sum1 = sum([self.board[i, i] for i in range(constants.BOARD_COLS)])
        diag_sum2 = sum([self.board[i, constants.BOARD_COLS - i - 1] for i in range(constants.BOARD_COLS)])
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
        for i in range(constants.BOARD_ROWS):
            for j in range(constants.BOARD_COLS):
                if self.board[i, j] == 0:
                    positions.append((i, j))  
        return positions


    """
    Marks the symbol on the board array

    Args: position -> Tuple of 2 numbers representing row and col values 

    """
    def updateState(self, position):
        self.board[position] = self.playerSymbol
        # Switch to another player
        self.playerSymbol *= -1

    # Resets the board
    @staticmethod
    def reset():
        global board
        global playerSymbol
        global isEnd

        board = np.zeros((constants.BOARD_ROWS, constants.BOARD_COLS))
        isEnd = False
        playerSymbol = 1
        global_variables.game_dict.clear()
        


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
            p1_action = self.p1.chooseAction(positions, self.board, self.playerSymbol)
            self.updateState(p1_action)
            return p1_action
        else:
            p2_action = self.p2.chooseAction(positions, self.board, self.playerSymbol)
            self.updateState(p2_action)
            return p2_action


    def postMatch(self,game_dict):
            try:
                r=requests.post(constants.url, json=game_dict)
                r.raise_for_status()
            except requests.exceptions.HTTPError as e:
                 print (e.response.text)


    """
    Method user for checking the board for a winner after every move and calling popup class for displaying it.
    Cheking for winner is done by winner() method defined above which returns 1/-1/None depending on the outcome

    Args: player --> Player names 
    Returns : 
    """
    def checkwin(self,player):
        global_variables.game_dict
        win = self.winner()
        if win is not None:
            if win == 1:
                PopupMessage(constants.app,player)
                global_variables.game_dict["winner"] = player
            elif win == -1:
                PopupMessage(constants.app,player)
                global_variables.game_dict["winner"] = player
            else:
                PopupMessage(constants.app,"Tie")
                global_variables.game_dict["winner"] = "None"
                  
            self.postMatch(global_variables.game_dict)
            self.reset()
            self.counter = 0
            return 0    
        

    def movesList(self,playerField):
        self.counter += 1
        try:
            global_variables.game_dict["moves"] += [{"moveNo": self.counter, "playedField": playerField}]
        except KeyError:
            pass
        

    """
    Used for separating/chosing gamemodes and assigning play orders

    GAMEMODES: 
            0- Player VS Player
            1- Player VS AI
            2- AI VS Player
    Args: gamemode --> int that represents our wanted gamemode
        
    """
    def play(self,gamemode):
        global_variables.game_dict["player1"]=self.p1.name
        global_variables.game_dict["player2"]=self.p2.name
        global_variables.game_dict["moves"] = []
        

        btn = GameScreen(constants.app)
        if(gamemode == 0): 
            while not self.isEnd:
                action = self.humanPlayerAction(1)
                btn.changeButtonState(action)
                self.movesList(constants.options_inv.get(action))
                if(self.checkwin(self.p1.name)==0): break

                action = self.humanPlayerAction(2)
                btn.changeButtonState(action)
                self.movesList(constants.options_inv.get(action))
                if(self.checkwin(self.p2.name)==0): break

        elif(gamemode == 1):
            while not self.isEnd:
                action = self.humanPlayerAction(1)
                btn.changeButtonState(action)
                self.movesList(constants.options_inv.get(action))
                if(self.checkwin(self.p1.name)==0): break   

                action = self.aiPlayerAction(2)
                btn.changeButtonState(action)
                self.movesList(constants.options_inv.get(action))
                if(self.checkwin(self.p2.name)==0): break

        elif(gamemode == 2):
            while not self.isEnd:
                action = self.aiPlayerAction(1)
                btn.changeButtonState(action)
                self.movesList(constants.options_inv.get(action))
                if(self.checkwin(self.p1.name)==0): break

                action = self.humanPlayerAction(2)
                btn.changeButtonState(action)
                self.movesList(constants.options_inv.get(action))
                if(self.checkwin(self.p2.name)==0): break
              


