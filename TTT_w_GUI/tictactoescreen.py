from constants import *
import mainmenuscreen
import historyscreen
import difficultyscreen
import human_player
#from ai_player import AiPlayer
#from human_player import HumanPlayer
import game_logic
#import sys



class TictactoeScreen(Frame):
    def __init__(self, container):
        super().__init__(container)
        #frame size and color
        self.frame = Frame(container, background=backgroundColor, width=windowWidth, height=windowHeight).place(x=0, y=0)
        
        #define buttons
        self.btnPvP = Button(self.frame,
         text="Player vs Player", 
         command=lambda:[self.destroy(), self.startPvPGame(), reset_state.set(1)])
        self.btnPvAI = Button(self.frame,
         text="Play vs BOT",
          command=lambda: [self.destroy(), difficultyscreen.DifficultyScreen(app)])
        self.btnHistory = Button(self.frame,
         text="History",
          command=lambda:[self.destroy(), historyscreen.HistoryScreen(app)])
        self.btnBack = Button(self.frame,
         text="Back",
          command=lambda:[self.destroy(), mainmenuscreen.MainMenuScreen(app)])
        
        #style buttons
        for btn in (self.btnPvP, self.btnPvAI, self.btnHistory, self.btnBack):
            setBtnStyle(btn)

        #place buttons
        self.btnPvP.place(x=initialXY, y=initialY4, width=btnWidth, height=btnHeight)
        self.btnPvAI.place(x=initialXY, y=initialY4 + incrementY4, width=btnWidth, height=btnHeight)
        self.btnHistory.place(x=initialXY, y=initialY4 + 2*incrementY4, width=btnWidth, height=btnHeight)
        self.btnBack.place(x=initialXY, y=initialY4 + 3*incrementY4, width=btnWidth, height=btnHeight)

    @staticmethod
    def startPvPGame():
        p1 = human_player.HumanPlayer("Player1")
        p2 = human_player.HumanPlayer("Player2")
        st = game_logic.GameLogic(p1, p2)
        st.play(0)

