from constants import *

class PopupMessage():
    def __init__(self, master,message):
        super().__init__()
        #global top
        self.message = message
        top = Toplevel(master, background=backgroundColor, width=popupWinWidth, height=popupWinHeight)
        global result
        
        if(message == "Tie"):
            pass
        else:
            message = "Winner is: {}!".format(message)

        popmessage = Label(top, text=message, font=("arial bold", 20))
        popmessage.pack(padx=25, pady=25)
        result = " "