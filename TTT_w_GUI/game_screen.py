from operator import ge
from constants import *
import global_variables
import tictactoescreen
import game_logic
import playvscomp_screen

"""
Class used for displaying Tic Tac Toe board

"""
class GameScreen(Frame):
    def __init__(self, container):
        super().__init__(container)
        #frame size and color
        self.frame = Frame(container, background=backgroundColor, width=windowWidth, height=windowHeight).place(x=0, y=0)
        self.buttons()
   

    def buttons(self):
        i = 1
        self.boardBtn = []
        for gridRow in range(3):
            self.boardBtn.append(gridRow)
            self.boardBtn[gridRow] = []
            for gridCol in range(3):
                self.boardBtn[gridRow].append(gridCol)
                self.boardBtn[gridRow][gridCol]=Button(self.frame, text=" ", font=("arial bold", 20), height=gsFieldBtnDim, width=gsFieldBtnDim*2,command=lambda x=i: playeraction.set(x))
                self.boardBtn[gridRow][gridCol].grid(row=gridRow, column=gridCol)
                i += 1
                if gridCol == 0:
                    self.boardBtn[gridRow][gridCol].grid(padx=(80, 0))
                if gridRow == 0:
                    self.boardBtn[gridRow][gridCol].grid(pady=(20, 0))
                if (gridRow == 1 or gridRow == 2) and gridCol != 0:
                    self.boardBtn[gridRow][gridCol].grid(padx=(0, 0))
                

        #other buttons
        self.btnReset = Button(self.frame,
        text="Restart",
        command=lambda:[self.destroy(),self.resetGame()])
        self.btnBack = Button(self.frame,
        text="Back",
        command=lambda:[self.destroy(),reset_state.set(0), self.resetGame(), tictactoescreen.TictactoeScreen(app)])
        
        #style buttonss
        for btn in (self.btnReset, self.btnBack):
            setBtnStyle(btn)
            
        #place buttons
        self.btnReset.place(x=gsInitialXY, y=4*gsInitialXY, width=gsBtnWidth, height=gsBtnHeight)
        self.btnBack.place(x=gsInitialXY + 132, y=4*gsInitialXY, width=gsBtnWidth, height=gsBtnHeight)
    
    """
    Function user for changing text on the buttons and assigning x or o value_max

    Receives action tuple and based on the coordinates in it and count number puts either X or O
    Params: action tuple (x,y) that tell us desired boadd position 

    """
    def changeButtonState(self,action):

        if(global_variables.count % 2 == 0):
            self.boardBtn[action[0]][action[1]].configure(text="X") 
        else:
            self.boardBtn[action[0]][action[1]].configure(text="O")
        global_variables.count +=1
        self.boardBtn[action[0]][action[1]].configure(state ="disabled")
      
    
    """
    resetGame function VISUALLY resets the board and starts new game depending on reset_state variable

    game_logic.GameLogic.reset() is used to reset the logic 

    reset_state is a global variable used to remeber our selected game mode so that in a case where we want to reset the game we don't have to go back to
    gamemode selection screen

    """
    def resetGame(self):

        for i in range(3):
            for j in range(3):
                self.boardBtn[i][j].configure(state = "normal")
                self.boardBtn[i][j].configure(text = " ")

        game_logic.GameLogic.reset()
        global_variables.count = 0
        if(reset_state.get() == 1): 
            tictactoescreen.TictactoeScreen.startPvPGame()
        elif(reset_state.get() == 2):
            playvscomp_screen.PlayVsCompScreen.startPvAIGameFirst()
        elif(reset_state.get() == 3):
            playvscomp_screen.PlayVsCompScreen.startPvAIGameSecond()
        elif(reset_state.get()== 4):
            tictactoescreen.TictactoeScreen.startReplay()


