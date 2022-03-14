from constants import *

"""
Class PopupMessage is currently only used to display winner name after game is finished

Args: You need to pass app which is a tkinter object and your message --> Currently hardcoded to only show winner message
"""
        
class PopupMessage():
    def __init__(self, root, message):
        super().__init__()
        
        self.message = message
        top = Toplevel(background=backgroundColor, width=popupWinWidth, height=popupWinHeight)
        top.transient(root)
        top.grab_set()
        #root.wait_window(top)
        
        global result
        
        if(message == "Tie"):
            pass
        else:
            message = "Winner is: {}!".format(message)

        popmessage = Label(top, text=message, font=("arial bold", 20), bg=backgroundColor)
        popmessage.pack(padx=25, pady=25)
        result = " "