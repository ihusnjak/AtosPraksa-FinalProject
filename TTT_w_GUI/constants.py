from tkinter import *

#define GUI constants
windowWidth = 400
windowHeight = 400
btnWidth = 300
btnHeight = 70
initialXY = 50
incrementY = btnHeight + initialXY
initialY4 = 23
incrementY4 = btnHeight + initialY4
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
#app.geometry(str(windowWidth) + "x" + str(windowHeight))
screenWidth = app.winfo_screenwidth()
screenHeight = app.winfo_screenheight()
xPosition = (screenWidth / 2) - (windowWidth / 2)
yPosition = (screenHeight / 2) - (windowHeight / 2)
app.title('AI GAMES')
app.geometry('%dx%d+%d+%d' % (windowWidth, windowHeight, xPosition, yPosition))
app.resizable(False, False)

def setBtnStyle(btn):
    btn["bg"] = btnBgColor
    btn["fg"] = btnFgColor
    btn["activebackground"] = btnActiveColor
    btn["activeforeground"] = btnFgColor
    btn["font"] = ('arial bold', 22)
    
#logic constants
reset_state = IntVar()
playeraction = IntVar()
difficulty = IntVar()
BOARD_ROWS = 3
BOARD_COLS = 3
options = {1: (0, 0), 2: (0, 1), 3: (0, 2),4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1), 9: (2, 2)}
options_inv = {(0, 0): 1,(0, 1): 2,(0, 2): 3,(1, 0): 4,(1, 1): 5,(1, 2): 6,(2, 0): 7,(2, 1): 8,(2, 2): 9}
p1_policies = {1: "policy_easy_p1",2: "policy_normal_p1", 3: "policy_hard_p1"}
p2_policies = {1: "policy_easy_p2",2: "policy_normal_p2", 3: "policy_hard_p2"}
url = "http://188.166.133.147:8081/"
game_url = "http://188.166.133.147:8081/1"

