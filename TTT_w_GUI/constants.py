from tkinter import *
import numpy as np

#define GUI constants
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

app = Tk()
app.geometry(str(windowWidth) + "x" + str(windowHeight))
app.resizable(False, False)

def setBtnStyle(btn):
    btn["bg"] = btnBgColor
    btn["fg"] = btnFgColor
    btn["activebackground"] = btnActiveColor
    btn["activeforeground"] = btnFgColor
    btn["font"] = ('arial bold', 22)
    
#logic constants
reset_state = IntVar()
count = 0
playeraction = IntVar()
BOARD_ROWS = 3
BOARD_COLS = 3
board = np.zeros((BOARD_ROWS, BOARD_COLS))

