from constants import *
import tictactoescreen

class HistoryScreen(Frame):
    def __init__(self, container):
        super().__init__(container)
        #frame size and color
        self.frame = Frame(container, background=backgroundColor, width=windowWidth, height=windowHeight).place(x=0, y=0)

        #define buttons
        self.btnClear = Button(self.frame,
         text="Clear",
           command=lambda: self.clearHistory)
        self.btnBack = Button(self.frame,
         text="Back",
          command=lambda:[self.destroy(), tictactoescreen.TictactoeScreen(app)])

        for btn in (self.btnClear, self.btnBack):
            setBtnStyle(btn)

        self.btnClear.place(x=gsInitialXY, y=4*gsInitialXY, width=gsBtnWidth, height=gsBtnHeight)
        self.btnBack.place(x=gsInitialXY + 132, y=4*gsInitialXY, width=gsBtnWidth, height=gsBtnHeight)
        
    def clearHistory():
        pass