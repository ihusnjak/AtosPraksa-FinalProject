from tkinter import *
import sys
from Constants import *

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
          command=lambda:[self.destroy(), PlayVsCompScreen(app)])
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
        
    """ @staticmethod
    def startPvPGame():
        p1 = HumanPlayer("Player1")
        p2 = HumanPlayer("Player2")
        st = State(p1, p2)
        st.play_human()"""

class PlayVsCompScreen(Frame):
    def __init__(self, container):
        super().__init__(container)
        #frame size and color
        self.frame = Frame(container, background=backgroundColor, width=windowWidth, height=windowHeight).place(x=0, y=0)

        #define buttons
        self.btnPlay1st = Button(self.frame,
         text="Start First", 
         command=lambda: self.startPvAIGame)
        self.btnPlay2nd = Button(self.frame,
         text="Start Second",
          command=lambda: self.startPvAIGame)
        self.btnBack = Button(self.frame,
         text="Back",
          command=lambda:[self.destroy(), TictactoeScreen(app)])

        #style buttons
        for btn in (self.btnPlay1st, self.btnPlay2nd, self.btnBack):
            setBtnStyle(btn)

        #place buttons
        self.btnPlay1st.place(x=initialXY, y=initialXY, width=btnWidth, height=btnHeight)
        self.btnPlay2nd.place(x=initialXY, y=initialXY + incrementY, width=btnWidth, height=btnHeight)
        self.btnBack.place(x=initialXY, y=initialXY + 2*incrementY, width=btnWidth, height=btnHeight)
        
    #needs to be implemented
    def startPvAIGame():
        return
    
class GameScreen(Frame):
    def __init__(self, container):
        super().__init__(container)
        #frame size and color
        self.frame = Frame(container, background=backgroundColor, width=windowWidth, height=windowHeight).place(x=0, y=0)
        self.buttons()
        
    def buttons(self):
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
          #command=lambda: self.resetGame)
          command=lambda: PopupMessage(app))
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
        
#popup window triggered when game ended
class PopupMessage:
    def __init__(self, master):
        super().__init__()
        #global top
        top = Toplevel(master, background=backgroundColor, width=popupWinWidth, height=popupWinHeight)
        
        """
        global result

        if result == "Tie":
            pass
        else:
            result = "Winner is: {}!".format(result)
            
        message = Label(top, text=result, font=("arial bold", 20), bg=backgroundColor)
        message.pack(padx=25, pady=25)
        result = " "
        """
        
        resultMessage = "Game Ended!"
        #resultMessage = gameEndMessage()
        message = Label(top, text=resultMessage, font=("arial bold", 20), bg=backgroundColor)
        message.pack(padx=25, pady=25)
        
#needs to be implemented
def gameEndMessage():
    return


class App(Tk):
    def __init__(self):
        super().__init__()
        # configure the root window
        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()
        xPosition = (screenWidth / 2) - (windowWidth / 2)
        yPosition = (screenHeight / 2) - (windowHeight / 2)
        self.title('AI GAMES')
        #self.geometry(str(windowWidth) + "x" + str(windowHeight))
        self.geometry('%dx%d+%d+%d' % (windowWidth, windowHeight, xPosition, yPosition))
        self.resizable(False, False)
        
if __name__ == "__main__":
    global app
    app = App()
    frame = MainMenuScreen(app)
    app.mainloop()