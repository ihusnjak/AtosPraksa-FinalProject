from tkinter import *
from turtle import color


#define constant
windowWidth = 400
windowHeight = 400
btnWidth = 300
btnHeight = 70
initialXY = 50
incrementY = btnHeight + initialXY


class MainMenuScreen(Frame):
    def __init__(self, container):
        super().__init__(container)
        #frame size and color
        self.frame = Frame(container, background="#8df542", width=windowWidth, height=windowHeight).place(x=0, y=0)
        
        #define buttons
        self.btnTictactoe = Button(self.frame, text="Tic Tac Toe")
        self.btnExit = Button(self.frame, text="Exit")
        
        #place buttons
        self.btnTictactoe.place(x=initialXY, y=initialXY, width=btnWidth, height=btnHeight)
        self.btnExit.place(x=initialXY, y=initialXY + incrementY, width=btnWidth, height=btnHeight)

class TictactoeScreen(Frame):
    def __init__(self, container):
        super().__init__(container)
        #frame size and color
        self.frame = Frame(container, background="#2856a6", width=windowWidth, height=windowHeight).place(x=0, y=0)
        
        #define buttons
        self.btnPvP = Button(self.frame, text="Player vs Player")
        self.btnPvAI = Button(self.frame, text="Play vs BOT")
        self.btnBack = Button(self.frame, text="Back")
        
        #place buttons
        self.btnPvP.place(x=initialXY, y=initialXY, width=btnWidth, height=btnHeight)
        self.btnPvAI.place(x=initialXY, y=initialXY + incrementY, width=btnWidth, height=btnHeight)
        self.btnBack.place(x=initialXY, y=initialXY + 2*incrementY, width=btnWidth, height=btnHeight)

class App(Tk):
    def __init__(self):
        super().__init__()
        # configure the root window
        self.title('AI GAMES')
        self.geometry(str(windowWidth) + "x" + str(windowHeight))
        self.resizable(False, False)


if __name__ == "__main__":
    app = App()
    frame = MainMenuScreen(app)
    app.mainloop()
