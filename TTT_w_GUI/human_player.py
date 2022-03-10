from constants import *
from player import Player

class HumanPlayer(Player):

    """
    Method that allows us to input on the board

    playeraction variable represents gui board where each button is one number starting from 1 
    app.wait_variable() is used to stop the program until button is pressed
    Args: 
    Returns: action --> tuple of row and col value that represents baord positon example: (0,0)
    """
    def chooseAction(self):
        global playeraction
        app.wait_variable(playeraction)
        action = (1,1)
    
        if(playeraction.get()==1):
            action = (0, 0)
        elif(playeraction.get() == 2):
            action = (0, 1)
        elif(playeraction.get() == 3):
            action = (0, 2)
        elif(playeraction.get() == 4):
            action = (1, 0)
        elif(playeraction.get() == 5):
            action = (1, 1)
        elif(playeraction.get() == 6):
            action = (1, 2)
        elif(playeraction.get() == 7):
            action = (2, 0)
        elif(playeraction.get() == 8):
            action = (2, 1)
        elif(playeraction.get() == 9):
            action = (2, 2)
      
        return action