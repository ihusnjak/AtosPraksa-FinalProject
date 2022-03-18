from constants import *
import tictactoescreen
import playvscomp_screen

class DifficultyScreen(Frame):
    def __init__(self, container):
        super().__init__(container)
        #frame size and color
        self.frame = Frame(container, background=backgroundColor, width=windowWidth, height=windowHeight).place(x=0, y=0)

        #define buttons
        difficulty.set(0)
        self.btnEasy = Button(self.frame,
         text="Easy",
         command=lambda: [self.destroy(),difficulty.set(1),playvscomp_screen.PlayVsCompScreen(app)])
        self.btnMedium = Button(self.frame,
         text="Medium",
         command=lambda: [self.destroy(),difficulty.set(2),playvscomp_screen.PlayVsCompScreen(app)])
        self.btnHard = Button(self.frame,
         text="Hard",
          command=lambda: [self.destroy(),difficulty.set(3),playvscomp_screen.PlayVsCompScreen(app)])
        self.btnBack = Button(self.frame,
         text="Back",
          command=lambda:[self.destroy(), tictactoescreen.TictactoeScreen(app)])

        #style buttons
        for btn in (self.btnEasy, self.btnMedium, self.btnHard, self.btnBack):
            setBtnStyle(btn)

        #place buttons
        self.btnEasy.place(x=initialXY, y=initialY4, width=btnWidth, height=btnHeight)
        self.btnMedium.place(x=initialXY, y=initialY4 + incrementY4, width=btnWidth, height=btnHeight)
        self.btnHard.place(x=initialXY, y=initialY4 + 2*incrementY4, width=btnWidth, height=btnHeight)
        self.btnBack.place(x=initialXY, y=initialY4 + 3*incrementY4, width=btnWidth, height=btnHeight)
        
