from constants import *
import mainmenuscreen
import difficultyscreen
from human_player import HumanPlayer
import game_logic
from replay_game import GameReplay
from game_screen import GameScreen
import constants

"""
Screen that appears after clicking Tic Tac Toe on the main menu, buttons activate functions that start various gamemodes and turn on the game screen.

Everybutton has a destroy function, reset_state variable that remembers the gamemode we want to reset and a function for starting the game.
NOTE: Probably will change after adding more play options

"""
class TictactoeScreen(Frame):
    def __init__(self, container):
        super().__init__(container)
        #frame size and color
        self.frame = Frame(container, background=backgroundColor, width=windowWidth, height=windowHeight).place(x=0, y=0)
        
        #define buttons
        self.btnPvP = Button(self.frame,
         text="Player vs Player", 
         command=lambda:[self.destroy(), reset_state.set(1),self.startPvPGame()])
        self.btnPvAI = Button(self.frame,
         text="Play vs BOT",
          #command=lambda: [self.destroy(), reset_state.set(2),self.startPvAIGame()])
          command=lambda: [self.destroy(), difficultyscreen.DifficultyScreen(app)])
        self.btnHistory = Button(self.frame,
         text="History")
        self.btnReplay = Button(self.frame,
         text="Show example game",
          command=lambda:[self.destroy(), reset_state.set(4) ,self.startReplay()])
        self.btnBack = Button(self.frame,
         text="Back",
          command=lambda:[self.destroy(), mainmenuscreen.MainMenuScreen(app)])
        
        #style buttons
        for btn in (self.btnPvP, self.btnPvAI, self.btnHistory, self.btnReplay, self.btnBack):
            setBtnStyle(btn)

        #place buttons
        self.btnPvP.place(x=initialXY, y=initialY4, width=btnWidth, height=btnHeight-20)
        self.btnPvAI.place(x=initialXY, y=initialY4 + incrementY4-20, width=btnWidth, height=btnHeight-20)
        self.btnHistory.place(x=initialXY, y=initialY4 + 2*incrementY4-40, width=btnWidth, height=btnHeight-20)
        self.btnReplay.place(x=initialXY, y=initialY4 + 3*incrementY4-60, width=btnWidth, height=btnHeight-20)
        self.btnBack.place(x=initialXY, y=initialY4 + 4*incrementY4-80, width=btnWidth, height=btnHeight-20)



    """
    We define p1 and p2 with their respective classes.
    If one or two players are Ai be sure to load correct policy, policy_p1 is used when ai plays first and vice versa

    st.play(number) is a function that starts a play function defined in game_logic.py file
    number --> represents the order of play, 0 is used for Player vs Player gamemode, 1 is when we are playing first vs AI and 2 when second
    
    """
    @staticmethod
    def startPvPGame():
        p1 = HumanPlayer("Player1")
        p2 = HumanPlayer("Player2")
        st = game_logic.GameLogic(p1,p2)
        st.play(0)

    @staticmethod
    def startReplay():
        data = {}
        replay = GameReplay()
        data = replay.connectToServer()
        replay.replayAGame(data)
         
