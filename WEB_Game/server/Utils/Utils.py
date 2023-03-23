from flask import abort

class Utils:

    @staticmethod
    def check_game_id(params:dict, session:dict):
        #Check that the game id is included on the request
        if len(params.keys()) == 0:
            abort(400, "You must specify the game id")

        #Check that the game id is correct and exists on the game list
        game_id = params.get('game_id')
        if game_id not in session.keys():
            abort(404, "Game ID not found")