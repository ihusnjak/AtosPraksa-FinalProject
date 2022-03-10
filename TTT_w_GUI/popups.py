from constants import *


"""
Class PopupMessage is currently only used to display winner name after game is finished

Args: You need to pass app which is a tkinter object and your message --> Currently hardcoded to only show winner message
"""
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