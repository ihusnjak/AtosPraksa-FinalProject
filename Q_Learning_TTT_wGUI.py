from msilib.schema import Font
from tkinter import *
import tkinter.font as font
from turtle import color
import sys


import numpy as np
import pickle


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

#logic constants
count = 0
playeraction = IntVar()
BOARD_ROWS = 3
BOARD_COLS = 3
result = " "

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
         command=lambda:[self.destroy(), self.startPvPGame()])
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

    @staticmethod
    def startPvPGame():
        p1 = HumanPlayer("Player1")
        p2 = HumanPlayer("Player2")
        st = State(p1, p2)
        st.play_human()
    
class GameScreen(Frame):
    def __init__(self, container):
        super().__init__(container)
        #frame size and color
        self.frame = Frame(container, background=backgroundColor, width=windowWidth, height=windowHeight).place(x=0, y=0)
        self.buttons()

        #define board buttons
    def buttons(self):
        self.btnB1 = Button(self.frame, text=" ", font=("arial bold", 20), height=gsFieldBtnDim, width=gsFieldBtnDim*2, command=lambda: playeraction.set(1))
        self.btnB2 = Button(self.frame, text=" ", font=("arial bold", 20), height=gsFieldBtnDim, width=gsFieldBtnDim*2, command=lambda: playeraction.set(2))
        self.btnB3 = Button(self.frame, text=" ", font=("arial bold", 20), height=gsFieldBtnDim, width=gsFieldBtnDim*2, command=lambda: playeraction.set(3))
        self.btnB4 = Button(self.frame, text=" ", font=("arial bold", 20), height=gsFieldBtnDim, width=gsFieldBtnDim*2, command=lambda: playeraction.set(4))
        self.btnB5 = Button(self.frame, text=" ", font=("arial bold", 20), height=gsFieldBtnDim, width=gsFieldBtnDim*2, command=lambda: playeraction.set(5))
        self.btnB6 = Button(self.frame, text=" ", font=("arial bold", 20), height=gsFieldBtnDim, width=gsFieldBtnDim*2, command=lambda: playeraction.set(6))
        self.btnB7 = Button(self.frame, text=" ", font=("arial bold", 20), height=gsFieldBtnDim, width=gsFieldBtnDim*2, command=lambda: playeraction.set(7))
        self.btnB8 = Button(self.frame, text=" ", font=("arial bold", 20), height=gsFieldBtnDim, width=gsFieldBtnDim*2, command=lambda: playeraction.set(8))
        self.btnB9 = Button(self.frame, text=" ", font=("arial bold", 20), height=gsFieldBtnDim, width=gsFieldBtnDim*2, command=lambda: playeraction.set(9))
        
        #other buttons
        self.btnReset = Button(self.frame,
        text="Restart",
        command=lambda: self.resetGame())
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
    
    """
    Function user for changing text on the buttons and assigning x or o value_max

    Params: action tuple (x,y) that tell us desired boadd position 

    """
    def changeButtonState(self,action):
        global count
        if(action[0] == 0 and action[1] == 0):
            if(count % 2 == 0):
                self.btnB1.configure(text="X")
                count +=1
            else:
                self.btnB1.configure(text="O")
                count +=1
            self.btnB1.configure(state ="disabled")
        elif(action[0] == 0 and action[1] == 1):
            if(count % 2 == 0):
                self.btnB2.configure(text="X")
                count +=1
            else:
                self.btnB2.configure(text="O")
                count +=1
            self.btnB2.configure(state ="disabled")
        elif(action[0] == 0 and action[1] == 2):
            if(count % 2 == 0):
                self.btnB3.configure(text="X")
                count +=1
            else:
                self.btnB3.configure(text="O")
                count +=1
            self.btnB3.configure(state ="disabled")
        elif(action[0] == 1 and action[1] == 0):
            if(count % 2 == 0):
                self.btnB4.configure(text="X")
                count +=1
            else:
                self.btnB4.configure(text="O")
                count +=1
            self.btnB4.configure(state ="disabled")
        elif(action[0] == 1 and action[1] == 1):
            if(count % 2 == 0):
                self.btnB5.configure(text="X")
                count +=1
            else:
                self.btnB5.configure(text="O")
                count +=1
            self.btnB5.configure(state ="disabled")
        elif(action[0] == 1 and action[1] == 2):
            if(count % 2 == 0):
               self.btnB6.configure(text="X")
               count +=1
            else:
                self.btnB6.configure(text="O")
                count +=1
            self.btnB6.configure(state ="disabled")
        elif(action[0] == 2 and action[1] == 0):
            if(count % 2 == 0):
                self.btnB7.configure(text="X")
                count +=1
            else:
                self.btnB7.configure(text="O")
                count +=1
            self.btnB7.configure(state ="disabled")
        elif(action[0] == 2 and action[1] == 1):
            if(count % 2 == 0):
                self.btnB8.configure(text="X")
                count +=1
            else:
                self.btnB8.configure(text="O")
                count +=1
            self.btnB8.configure(state ="disabled")
        elif(action[0] == 2 and action[1] == 2):
            if(count % 2 == 0):
                self.btnB9.configure(text="X")
                count +=1
            else:
                self.btnB9.configure(text="O")
                count +=1
            self.btnB9.configure(state ="disabled")
        else:
            print("Invalid input") 
    #needs to be implemented
    def resetGame(self):
        for btn in (self.btnB1,self.btnB2,self.btnB3,self.btnB4,self.btnB5,self.btnB6,self.btnB7,self.btnB8,self.btnB9):
            btn["text"]=" "
            btn["state"] = "normal"
        State.reset()
        TictactoeScreen.startPvPGame()
    #needs to be implemented
    def btnClick():
        return
        
#popup window triggered when game ended
class PopupMessage():
    def __init__(self, master):
        super().__init__()
        #global top
        top = Toplevel(master, background=backgroundColor, width=popupWinWidth, height=popupWinHeight)
        global result

        if result == "Tie":
            pass
        else:
            result = "Winner is: {}!".format(result)
            
        message = Label(top, text=result, font=("arial bold", 20))
        message.pack(padx=25, pady=25)
        result = " "
        
class State:
    def __init__(self, p1, p2):
        self.board = np.zeros((BOARD_ROWS, BOARD_COLS))
        self.p1 = p1
        self.p2 = p2
        self.isEnd = False
        self.boardHash = None
        # init p1 plays first
        self.playerSymbol = 1

    def getHash(self):
        self.boardHash = str(self.board.reshape(BOARD_COLS * BOARD_ROWS))
        return self.boardHash


    def winner(self):
        # Checking rows
        for i in range(BOARD_ROWS):
            if sum(self.board[i, :]) == 3:
                self.isEnd = True
                return 1
            if sum(self.board[i, :]) == -3:
                self.isEnd = True
                return -1
        # Checking columns
        for i in range(BOARD_COLS):
            if sum(self.board[:, i]) == 3:
                self.isEnd = True
                return 1
            if sum(self.board[:, i]) == -3:
                self.isEnd = True
                return -1
        # Checking diagonals
        diag_sum1 = sum([self.board[i, i] for i in range(BOARD_COLS)])
        diag_sum2 = sum([self.board[i, BOARD_COLS - i - 1] for i in range(BOARD_COLS)])
        diag_sum = max(abs(diag_sum1), abs(diag_sum2))
        if diag_sum == 3:
            self.isEnd = True
            if diag_sum1 == 3 or diag_sum2 == 3:
                return 1
            else:
                return -1

        # If there are no available positions its a tie
        if len(self.availablePositions()) == 0:
            self.isEnd = True
            return 0

        self.isEnd = False
        return None

    """
    Method that keeps track of free and taken spots on the board

    Args: None
    Returns: Positions array which contains the positions that are marked by either x or o
    """
    def availablePositions(self):
        positions = []
        for i in range(BOARD_ROWS):
            for j in range(BOARD_COLS):
                if self.board[i, j] == 0:
                    positions.append((i, j))  
        return positions


    def updateState(self, position):
        self.board[position] = self.playerSymbol
        # Switch to another player
        self.playerSymbol = -1 if self.playerSymbol == 1 else 1

    # Resets the board
    @staticmethod
    def reset():
        board = np.zeros((BOARD_ROWS, BOARD_COLS))
        boardHash = None
        isEnd = False
        playerSymbol = -1
        global count 
        count = 0
    
    """
    #Working on Player vs AI
    # Play vs AI , play second
    def play_second(self):
        btn = GameScreen(app)
        while not self.isEnd:

            positions = self.availablePositions()
            p1_action = self.p1.chooseAction(positions, self.board, self.playerSymbol)
            
            
            # take action and upate board state
            self.updateState(p1_action)
            btn.changeButtonState(p1_action)
            # check board status if it is end
            win = self.winner()
            if win is not None:
                if win == 1:
                    print(self.p1.name, "wins!")
                else:
                    print("tie!")
                State.reset()
                break

            else:
                p2_action = self.p2.chooseAction()
                               
                self.updateState(p2_action)
                btn.changeButtonState(p2_action)
                win = self.winner()

                if win is not None:
                    if win == -1:
                        print(self.p2.name, "wins!")
                    else:
                        print("tie!")
                    State.reset()
                    break
    """
    def play_human(self):
        global result
        btn = GameScreen(app)
        while not self.isEnd:

            p1_action = self.p1.chooseAction()
            # take action and upate board state
            self.updateState(p1_action)
            btn.changeButtonState(p1_action)
            # check board status if it is end
            win = self.winner()
            if win is not None:
                if win == 1:

                    result = self.p1.name 
                    PopupMessage(app)
                    
                else:
                    result = "Tie" 
                    PopupMessage(app)
                self.reset()
                break

            else:
                p2_action = self.p2.chooseAction()
                               
                self.updateState(p2_action)
                btn.changeButtonState(p2_action)
                win = self.winner()

                if win is not None:
                    if win == -1:
                        result = self.p2.name 
                        PopupMessage(app)
                    else:
                        result = "Tie" 
                        PopupMessage(app)
                    self.reset()
                    break

class Player:
    def __init__(self, name, exp_rate=0.3):
        self.name = name
        self.states = []  # record all positions taken
        self.lr = 0.2
        self.exp_rate = exp_rate
        self.decay_gamma = 0.9
        self.states_value = {}  # state -> value

    def getHash(self, board):
        boardHash = str(board.reshape(BOARD_COLS * BOARD_ROWS))
        return boardHash


    """
    chooseAction method 

    Args: positions --> array of available places on the board
          current_board --> array that represents current board state
          symbol --> char that represents current player
    Returns: action --> puts x or o on the board
    """

    def chooseAction(self, positions, current_board, symbol):
        if np.random.uniform(0, 1) <= self.exp_rate:
            # take random action
            idx = np.random.choice(len(positions))
            action = positions[idx]
        else:
            value_max = -999
            for p in positions:
                next_board = current_board.copy()
                next_board[p] = symbol
                next_boardHash = self.getHash(next_board)
                value = 0 if self.states_value.get(next_boardHash) is None else self.states_value.get(next_boardHash)

                if value >= value_max:
                    value_max = value
                    action = p
        return action

    # Append a hash state
    def addState(self, state):
        self.states.append(state)

    def reset(self):
        self.states = []

    # Saves policy after training, used only while training , not required for overall usage
    def savePolicy(self):
        fw = open('policy_' + str(self.name), 'wb')
        pickle.dump(self.states_value, fw)
        fw.close()

    # Loads policy after training, used only while training , not required for overall usage
    def loadPolicy(self, file):
        fr = open(file, 'rb')
        self.states_value = pickle.load(fr)
        fr.close()

#Represents class for Human player
class HumanPlayer:
    def __init__(self, name):
        self.name = name

    """
    Method that allows us to input on the board

    Args: 
    Returns: action --> index where our input is on the board
    """
    def chooseAction(self):
        global playeraction
        app.wait_variable(playeraction)
        action = (1,1)

        if(playeraction.get()==1):
            action = (0, 0)
        elif(playeraction.get() == 2):
            action = (0, 1)
        elif(playeraction.get() == 3):
            action = (0, 2)
        elif(playeraction.get() == 4):
            action = (1, 0)
        elif(playeraction.get() == 5):
            action = (1, 1)
        elif(playeraction.get() == 6):
            action = (1, 2)
        elif(playeraction.get() == 7):
            action = (2, 0)
        elif(playeraction.get() == 8):
            action = (2, 1)
        elif(playeraction.get() == 9):
            action = (2, 2)
        else:
            print("Invalid input")
        
        return action

if __name__ == "__main__":
    frame = MainMenuScreen(app)
    app.mainloop()