import mainmenuscreen
from constants import *

"""
            TIC TAC TOE PYTHON

Running the main starts the program by initializing the main menu located in mainmenuscreen.py file. In it atm we have 2 buttons , 
one is for exiting the program and other one is the Tic Tac Toe game button. Second button initiates quitProgram() method which shuts down the program
while the second button initializes TictactoeScreen class.

TictactoeScreen currently has 3 buttons, one is exit just like in the main menu screen other two are for selecting currently available gamemodes.
In the TictactoeScreen class we find 2 static methods : startPvPGame() and startPvAIGame() which are referenced in their respective Player vs Player button and Player vs AI.
Clicking on the button starts one of the methods which in turn initiate the Tictactoe game. But how?

First the PvP game: 
    After calling the method in its body two objects are created , p1 and p2. Both are HumanPlayer class which extends Player class. Because it extends Player class we need to
    give it a "name" in our case its Player 1 and Player 2. This can be manipulated in any way and is a potential future upgrade where players can chose their own name
    in the GUI. 

    After that object of GameLogic class is created. GameLogic class contains methods for checking win conditions, choosing actions etc. As a parametar it receives Player 1
    and Player 2 objects. Using GameLogic object we initialize play() method. play() method is defined in game_logic.py file and as a parametar we give it a number that 
    represents our wanted gamemode and play order. In Player vs Player order doesn't matter but gamemode does. 

    **In game_logic file there are explanations of what every method does in case you want to make changes.

    Here is the list of current gamemodes and orders:   0- Player VS Player
                                                        1- Player VS AI
                                                        2- AI VS Player

    Initialization of play() method creates GameScreen class object and now we have a tic tac toe game board to play with.

    After selecting gamemode by clicking on a button in previous menu we also give reset_state variable value of 1 or 2 depending on the chosen menu.
    reset_state is important because it allows us to remeber the selected game mode so that in case where we want to restart the game we don't have to re-select the gamemode.

    ..... TO BE CONTINUED




"""
if __name__ == "__main__":
    frame = mainmenuscreen.MainMenuScreen(app)
    app.mainloop()
