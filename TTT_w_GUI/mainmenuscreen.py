from constants import *
import tictactoescreen 

class MainMenuScreen(Frame):
    def __init__(self, container):
        super().__init__(container)
        #frame size and color
        self.frame = Frame(container, background=backgroundColor, width=windowWidth, height=windowHeight).place(x=0, y=0)
        
        #define buttons
        self.btnTictactoe = Button(self.frame,
         text="Tic Tac Toe", 
         command=lambda:[self.destroy(), tictactoescreen.TictactoeScreen(app),reset_state.set(0)])
        self.btnExit = Button(self.frame,
         text="Exit",
         command=lambda:[self.quitProgram()])
        
        #style buttons
        for btn in (self.btnTictactoe, self.btnExit):
            setBtnStyle(btn)

        #place buttons
        self.btnTictactoe.place(x=initialXY, y=initialXY, width=btnWidth, height=btnHeight)
        self.btnExit.place(x=initialXY, y=initialXY + incrementY, width=btnWidth, height=btnHeight)
    
    def quitProgram(self):
        quit()

