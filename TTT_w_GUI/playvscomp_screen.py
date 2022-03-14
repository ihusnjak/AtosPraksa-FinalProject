from constants import *
import difficultyscreen
from ai_player import AiPlayer
from human_player import HumanPlayer
import game_logic

class PlayVsCompScreen(Frame):
    def __init__(self, container):
        super().__init__(container)
        #frame size and color
        self.frame = Frame(container, background=backgroundColor, width=windowWidth, height=windowHeight).place(x=0, y=0)

        #define buttons
        self.btnPlay1st = Button(self.frame,
         text="Start First", 
          command=lambda: [self.destroy(), reset_state.set(2),self.startPvAIGame()])
        self.btnPlay2nd = Button(self.frame,
         text="Start Second",
          command=lambda: [self.destroy(), reset_state.set(2),self.startPvAIGame()])
        self.btnBack = Button(self.frame,
         text="Back",
          command=lambda:[self.destroy(), difficultyscreen.DifficultyScreen(app)])

        #style buttons
        for btn in (self.btnPlay1st, self.btnPlay2nd, self.btnBack):
            setBtnStyle(btn)

        #place buttons
        self.btnPlay1st.place(x=initialXY, y=initialXY, width=btnWidth, height=btnHeight)
        self.btnPlay2nd.place(x=initialXY, y=initialXY + incrementY, width=btnWidth, height=btnHeight)
        self.btnBack.place(x=initialXY, y=initialXY + 2*incrementY, width=btnWidth, height=btnHeight)
        
    @staticmethod
    def startPvAIGame():     
        p1 = HumanPlayer("Player")
        p2 = AiPlayer("Computer")
        p2.loadPolicy("policy_p1")
        st = game_logic.GameLogic(p1, p2)
        st.play(2)
