from msilib.schema import Font
from tkinter import *
import tkinter.font as font
from turtle import color, width
import sys

windowWidth = 400
windowHeight = 400
btnWidth = 100
btnHeight = 50
fieldBtnDim = 2
initialXY = 80
backgroundColor = "#C1E3FF"

btnBgColor = "#7CC6FE"
btnFgColor = "#FFFFFF"
btnActiveColor = "#3B83BA"

def setBtnStyle(btn):
    btn["bg"] = btnBgColor
    btn["fg"] = btnFgColor
    btn["activebackground"] = btnActiveColor
    btn["activeforeground"] = btnFgColor
    btn["font"] = ('arial bold', 14)

class GameScreen(Frame):
    def __init__(self, container):
        super().__init__(container)
        #frame size and color
        self.frame = Frame(container, background=backgroundColor, width=windowWidth, height=windowHeight).place(x=0, y=0)
        
        #define board buttons
        self.btnB1 = Button(self.frame, text=" ", font=("arial bold", 20), height=fieldBtnDim, width=fieldBtnDim*2, command=lambda: self.btnClick)
        self.btnB2 = Button(self.frame, text=" ", font=("arial bold", 20), height=fieldBtnDim, width=fieldBtnDim*2, command=lambda: self.btnClick)
        self.btnB3 = Button(self.frame, text=" ", font=("arial bold", 20), height=fieldBtnDim, width=fieldBtnDim*2, command=lambda: self.btnClick)
        self.btnB4 = Button(self.frame, text=" ", font=("arial bold", 20), height=fieldBtnDim, width=fieldBtnDim*2, command=lambda: self.btnClick)
        self.btnB5 = Button(self.frame, text=" ", font=("arial bold", 20), height=fieldBtnDim, width=fieldBtnDim*2, command=lambda: self.btnClick)
        self.btnB6 = Button(self.frame, text=" ", font=("arial bold", 20), height=fieldBtnDim, width=fieldBtnDim*2, command=lambda: self.btnClick)
        self.btnB7 = Button(self.frame, text=" ", font=("arial bold", 20), height=fieldBtnDim, width=fieldBtnDim*2, command=lambda: self.btnClick)
        self.btnB8 = Button(self.frame, text=" ", font=("arial bold", 20), height=fieldBtnDim, width=fieldBtnDim*2, command=lambda: self.btnClick)
        self.btnB9 = Button(self.frame, text=" ", font=("arial bold", 20), height=fieldBtnDim, width=fieldBtnDim*2, command=lambda: self.btnClick)
        
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
        self.btnReset.place(x=initialXY, y=4*initialXY, width=btnWidth, height=btnHeight)
        self.btnBack.place(x=initialXY + 132, y=4*initialXY, width=btnWidth, height=btnHeight)
    
    #needs to be implemented
    def resetGame():
        return
    #needs to be implemented
    def btnClick():
        return
     
class TictactoeScreen():
    pass

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
    frame = GameScreen(app)
    app.mainloop()
