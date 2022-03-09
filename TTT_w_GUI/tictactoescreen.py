from constants import *
import mainmenuscreen
import human_player
from ai_player import AiPlayer
from human_player import HumanPlayer
import game_logic
import sys



class TictactoeScreen(Frame):
    def __init__(self, container):
        super().__init__(container)
        #frame size and color
        self.frame = Frame(container, background=backgroundColor, width=windowWidth, height=windowHeight).place(x=0, y=0)
        
        #define buttons
        self.btnPvP = Button(self.frame,
         text="Player vs Player", 
         command=lambda:[self.destroy(), self.startPvPGame()])
        self.btnPvAI = Button(self.frame,
         text="Play vs BOT",
          command=lambda: [self.destroy(), self.startPvAIGame()])
        self.btnBack = Button(self.frame,
         text="Back",
          command=lambda:[self.destroy(), mainmenuscreen.MainMenuScreen(app)])
        
        #style buttons
        for btn in (self.btnPvP, self.btnPvAI, self.btnBack):
            setBtnStyle(btn)

        #place buttons
        self.btnPvP.place(x=initialXY, y=initialXY, width=btnWidth, height=btnHeight)
        self.btnPvAI.place(x=initialXY, y=initialXY + incrementY, width=btnWidth, height=btnHeight)
        self.btnBack.place(x=initialXY, y=initialXY + 2*incrementY, width=btnWidth, height=btnHeight)

    #needs to be implemented
    @staticmethod
    def startPvAIGame():
        p1 = AiPlayer("Computer")
        p1.loadPolicy("policy_p2")
        p2 = HumanPlayer("Player")
        st = game_logic.GameLogic(p1, p2)
        st.play(2)


    @staticmethod
    def startPvPGame():
        p1 = human_player.HumanPlayer("Player1")
        p2 = human_player.HumanPlayer("Player2")
        st = game_logic.GameLogic(p1, p2)
        st.play(0)

