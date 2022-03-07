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
gsBtnWidth = 100
gsBtnHeight = 50
gsFieldBtnDim = 2
gsInitialXY = 80
popupWinWidth = 300
popupWinHeight = 50
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
         command=lambda:[self.destroy(), GameScreen(app)])
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
    def startPvAIGame():
        return
    
class GameScreen(Frame):
    def __init__(self, container):
        super().__init__(container)
        #frame size and color
        self.frame = Frame(container, background=backgroundColor, width=windowWidth, height=windowHeight).place(x=0, y=0)
        
        #define board buttons
        self.btnB1 = Button(self.frame, text=" ", font=("arial bold", 20), height=gsFieldBtnDim, width=gsFieldBtnDim*2, command=lambda: self.btnClick)
        self.btnB2 = Button(self.frame, text=" ", font=("arial bold", 20), height=gsFieldBtnDim, width=gsFieldBtnDim*2, command=lambda: self.btnClick)
        self.btnB3 = Button(self.frame, text=" ", font=("arial bold", 20), height=gsFieldBtnDim, width=gsFieldBtnDim*2, command=lambda: self.btnClick)
        self.btnB4 = Button(self.frame, text=" ", font=("arial bold", 20), height=gsFieldBtnDim, width=gsFieldBtnDim*2, command=lambda: self.btnClick)
        self.btnB5 = Button(self.frame, text=" ", font=("arial bold", 20), height=gsFieldBtnDim, width=gsFieldBtnDim*2, command=lambda: self.btnClick)
        self.btnB6 = Button(self.frame, text=" ", font=("arial bold", 20), height=gsFieldBtnDim, width=gsFieldBtnDim*2, command=lambda: self.btnClick)
        self.btnB7 = Button(self.frame, text=" ", font=("arial bold", 20), height=gsFieldBtnDim, width=gsFieldBtnDim*2, command=lambda: self.btnClick)
        self.btnB8 = Button(self.frame, text=" ", font=("arial bold", 20), height=gsFieldBtnDim, width=gsFieldBtnDim*2, command=lambda: self.btnClick)
        self.btnB9 = Button(self.frame, text=" ", font=("arial bold", 20), height=gsFieldBtnDim, width=gsFieldBtnDim*2, command=lambda: self.btnClick)
        
        #other buttons
        self.btnReset = Button(self.frame,
         text="Restart",
          command=lambda: self.resetGame)
        self.btnBack = Button(self.frame,
         text="Back",
          command=lambda:[self.destroy(), TictactoeScreen(app)])
        
        #style buttons
        for btn in (self.btnReset, self.btnBack):
            setBtnStyle(btn)
            
        #grid board buttons
        self.btnB1.grid(row=1, column=1, padx=(80, 0), pady=(20, 0))
        self.btnB2.grid(row=1, column=2, pady=(20, 0))
        self.btnB3.grid(row=1, column=3, pady=(20, 0))
        self.btnB4.grid(row=2, column=1, padx=(80, 0))
        self.btnB5.grid(row=2, column=2, padx=(0, 0))
        self.btnB6.grid(row=2, column=3, padx=(0, 0))
        self.btnB7.grid(row=3, column=1, padx=(80, 0))
        self.btnB8.grid(row=3, column=2, padx=(0, 0))
        self.btnB9.grid(row=3, column=3, padx=(0, 0))
            
        #place buttons
        self.btnReset.place(x=gsInitialXY, y=4*gsInitialXY, width=gsBtnWidth, height=gsBtnHeight)
        self.btnBack.place(x=gsInitialXY + 132, y=4*gsInitialXY, width=gsBtnWidth, height=gsBtnHeight)
    
    #needs to be implemented
    def resetGame():
        return
    #needs to be implemented
    def btnClick():
        return
        
#popup window triggered when game ended
class PopupMessage:
    def __init__(self, master):
        super().__init__()
        #global top
        top = Toplevel(master, background=backgroundColor, width=popupWinWidth, height=popupWinHeight)
        
        resultMessage = gameEndMessage()
        message = Label(top, text=resultMessage, font=("arial bold", 20))
        message.pack(padx=25, pady=25)
        
#needs to be implemented
def gameEndMessage():
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