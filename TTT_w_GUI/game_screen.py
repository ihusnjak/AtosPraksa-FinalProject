from constants import *
import tictactoescreen
import game_logic

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
        command=lambda:[self.destroy(),self.resetGame()],)
        self.btnBack = Button(self.frame,
        text="Back",
        command=lambda:[self.destroy(),tictactoescreen.TictactoeScreen(app)],)
        
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
            else:
                self.btnB1.configure(text="O")
            count +=1
            self.btnB1.configure(state ="disabled")
        elif(action[0] == 0 and action[1] == 1):
            if(count % 2 == 0):
                self.btnB2.configure(text="X")    
            else:
                self.btnB2.configure(text="O")
            count +=1  
            self.btnB2.configure(state ="disabled")
        elif(action[0] == 0 and action[1] == 2):
            if(count % 2 == 0):
                self.btnB3.configure(text="X")    
            else:
                self.btnB3.configure(text="O")
            count +=1    
            self.btnB3.configure(state ="disabled")
        elif(action[0] == 1 and action[1] == 0):
            if(count % 2 == 0):
                self.btnB4.configure(text="X")    
            else:
                self.btnB4.configure(text="O")
            count +=1  
            self.btnB4.configure(state ="disabled")
        elif(action[0] == 1 and action[1] == 1):
            if(count % 2 == 0):
                self.btnB5.configure(text="X")    
            else:
                self.btnB5.configure(text="O")
            count +=1    
            self.btnB5.configure(state ="disabled")
        elif(action[0] == 1 and action[1] == 2):
            if(count % 2 == 0):
               self.btnB6.configure(text="X")    
            else:
                self.btnB6.configure(text="O")
            count +=1    
            self.btnB6.configure(state ="disabled")
        elif(action[0] == 2 and action[1] == 0):
            if(count % 2 == 0):
                self.btnB7.configure(text="X")    
            else:
                self.btnB7.configure(text="O")
            count +=1    
            self.btnB7.configure(state ="disabled")
        elif(action[0] == 2 and action[1] == 1):
            if(count % 2 == 0):
                self.btnB8.configure(text="X")    
            else:
                self.btnB8.configure(text="O")
            count +=1    
            self.btnB8.configure(state ="disabled")
        elif(action[0] == 2 and action[1] == 2):
            if(count % 2 == 0):
                self.btnB9.configure(text="X")    
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
        global count
        count = 0
        game_logic.GameLogic.reset()
        tictactoescreen.TictactoeScreen.startPvPGame()


