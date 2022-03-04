from msilib.schema import Font
from tkinter import *
import tkinter.font as font
from turtle import color
import sys



#define constant
windowWidth = 400
windowHeight = 400
btnWidth = 300
btnHeight = 70
initialXY = 50
incrementY = btnHeight + initialXY
backgroundColor = "#C1E3FF"

btnBgColor = "#7CC6FE"
btnFgColor = "#FFFFFF"
btnActiveColor = "#3B83BA"


def setBtnStyle(btn):
    btn["bg"] = btnBgColor
    btn["fg"] = btnFgColor
    btn["activebackground"] = btnActiveColor
    btn["activeforeground"] = btnFgColor
    btn["font"] = ('arial bold', 22)

class MainMenuScreen(Frame):
    def __init__(self, container):
        super().__init__(container)
        #frame size and color
        self.frame = Frame(container, background=backgroundColor, width=windowWidth, height=windowHeight).place(x=0, y=0)
        
        #define buttons
        self.btnTictactoe = Button(self.frame,
         text="Tic Tac Toe", 
         command=lambda:[self.destroy(), TictactoeScreen(app)])
        self.btnExit = Button(self.frame,
         text="Exit",
         command=self.quitProgram)
        
        #style buttons
        for btn in (self.btnTictactoe, self.btnExit):
            setBtnStyle(btn)

        #place buttons
        self.btnTictactoe.place(x=initialXY, y=initialXY, width=btnWidth, height=btnHeight)
        self.btnExit.place(x=initialXY, y=initialXY + incrementY, width=btnWidth, height=btnHeight)
    
    def quitProgram(self):
        sys.exit(0)

class TictactoeScreen(Frame):
    def __init__(self, container):
        super().__init__(container)
        #frame size and color
        self.frame = Frame(container, background=backgroundColor, width=windowWidth, height=windowHeight).place(x=0, y=0)
        
        #define buttons
        self.btnPvP = Button(self.frame,
         text="Player vs Player", 
         command=lambda: self.startPvPGame)
        self.btnPvAI = Button(self.frame,
         text="Play vs BOT",
          command=lambda: self.startPvAIGame)
        self.btnBack = Button(self.frame,
         text="Back",
          command=lambda:[self.destroy(), MainMenuScreen(app)])
        
        #style buttons
        for btn in (self.btnPvP, self.btnPvAI, self.btnBack):
            setBtnStyle(btn)

        #place buttons
        self.btnPvP.place(x=initialXY, y=initialXY, width=btnWidth, height=btnHeight)
        self.btnPvAI.place(x=initialXY, y=initialXY + incrementY, width=btnWidth, height=btnHeight)
        self.btnBack.place(x=initialXY, y=initialXY + 2*incrementY, width=btnWidth, height=btnHeight)

    #needs to be implemented
    def startPvPGame():
        return
    #needs to be implemented
    def startPvAIGame():
        return

class App(Tk):
    def __init__(self):
        super().__init__()
        # configure the root window
        self.title('AI GAMES')
        self.geometry(str(windowWidth) + "x" + str(windowHeight))
        self.resizable(False, False)


if __name__ == "__main__":
    global app
    app = App()
    frame = MainMenuScreen(app)
    app.mainloop()
