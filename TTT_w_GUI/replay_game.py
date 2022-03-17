
from urllib.request import urlopen
from game_screen import GameScreen
import constants
import json

class GameReplay():

    def connectToServer(self):
        response = urlopen(constants.game_url)
        data_json = json.loads(response.read())

        return data_json

    def replayAGame(self,data):
        btn = GameScreen(constants.app)
        constants.app.update()
        for i in range(len(data["moves"])):           
            action = constants.options.get(data["moves"][i]["affected_field"]) 
            btn.after(1000,btn.changeButtonState(action))
            constants.app.update()

            
            





