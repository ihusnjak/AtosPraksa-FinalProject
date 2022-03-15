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
          command=lambda: [self.destroy(), reset_state.set(2),self.startPvAIGameFirst()])
        self.btnPlay2nd = Button(self.frame,
         text="Start Second",
          command=lambda: [self.destroy(), reset_state.set(3),self.startPvAIGameSecond()])
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


    """
    We define p1 and p2 with their respective classes.
    Each player needs their respecitve policy loaded so when AI goes first it needs policy_p1.

    st.play(number) is a function that starts a play function defined in game_logic.py file
    number --> represents the order of play, 0 is used for Player vs Player gamemode, 1 is when we are playing first vs AI and 2 when second
    
    """

    @staticmethod
    def startPvAIGameFirst():     
        p1 = HumanPlayer("Player")
        p2 = AiPlayer("Computer")
        p2.loadPolicy("policy_p2")
        st = game_logic.GameLogic(p1, p2)
        st.play(1)
    
    @staticmethod
    def startPvAIGameSecond():     
        p2 = HumanPlayer("Player")
        p1 = AiPlayer("Computer")
        p1.loadPolicy("policy_p1")
        st = game_logic.GameLogic(p1, p2)
        st.play(2)
