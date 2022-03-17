import constants
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
        constants.app.wait_variable(constants.playeraction)
        action = (1,1)

        for i in range(10):
            action = constants.options.get(constants.playeraction.get())

        return action