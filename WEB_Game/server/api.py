from flask import Flask, request, jsonify, abort
from flask_cors import CORS, cross_origin
from random import randrange
import os
import json
import time
from GL.Game import Game
from Utils.Utils import Utils

tctctoe_server = Flask(__name__)
#tctctoe_server.secret_key = os.environ.get('secret_key')
tctctoe_server.secret_key = 'secretkey' #ONLY DURING DEVELOPMENT
#Adding CORS for the app
CORS(tctctoe_server)
game_sessions= dict()



@tctctoe_server.route('/get-game-id', methods = ['GET'])
@cross_origin(origin="*", headers=["Content-Type"])
def create_game_instance():

    #Generate game id
    def generate_game_id() -> str:
        game_id:str = ""
        for i in range(8):
            #Generates a randon number
            randNum = randrange(1,8)
            game_id += str(randNum)
        return game_id
    
    game_id = generate_game_id()
    #Add new game instance that could be referenced by the game_id
    game_sessions[game_id] = Game()
    print(game_id)
    return jsonify({'game_id': game_id})




@tctctoe_server.route('/get-board', methods = ['GET'])
@cross_origin(origin="*", headers=["Content-Type"])
def get_board():
    #Get the query parameters to get the game id
    params = request.args
    #Check the game id information is correct
    Utils.check_game_id(params, game_sessions)
    game:Game = game_sessions.get(params.get('game_id'))
    return jsonify({'board' : game.get_board()})





@tctctoe_server.route('/winner', methods = ['GET'])
@cross_origin(origin="*", headers=["Content-Type"])
def get_winner():
    #Get the query parameters to get the game id
    params = request.args
    #Check the game id information is correct
    Utils.check_game_id(params, game_sessions)
    game:Game = game_sessions.get(params.get('game_id'))

    winner = game.winner
    if game.numbers_In_Board() == 0 and winner == None:
        winner = "tie"
    return jsonify({'winner' : winner})





@tctctoe_server.route('/move', methods = ['POST'])
@cross_origin(origin="*", headers=["Content-Type"])
def user_move():
    #Get the query parameters to get the game id
    params = request.args
    #Check the game id information is correct
    Utils.check_game_id(params, game_sessions)
    game:Game = game_sessions.get(params.get('game_id'))

    move = None
    try:
        move = int(json.loads(request.data).get('move'))
    except ValueError:
        abort(400, "Incorrect Move")

    #Validate that the move is correct
    if not game.is_num_in_Board(move):
        abort(400, "Incorrect Move")

    game.enterMove(move)
    game.victory()
    return jsonify({'board' : game.get_board()})






@tctctoe_server.route('/machine-move', methods = ['GET'])
@cross_origin(origin="*", headers=["Content-Type"])
def machine_move():
    #Get the query parameters to get the game level and id
    params = request.args
    #Check the game id information is correct
    Utils.check_game_id(params, game_sessions)
    game:Game = game_sessions.get(params.get('game_id'))

    #Game levels
    levels = ['normal', 'advanced']

    if len(params.keys()) == 1 or len(params.keys()) == 0:
        abort(400, "You must specify the game level and game id")
    
    #Check that the level key is sent
    if 'level' not in params.keys():
        abort(404, "No level requested")

    gameLevel = params.get('level')
    if gameLevel not in levels:
        abort(404, "Level requested doesn't exist")

    #Asign the level to the game instance
    game.level = gameLevel

    game.machineMove()
    game.victory()
    time.sleep(0.3)
    return jsonify({'board' : game.get_board()})





@tctctoe_server.route("/restart", methods = ['PUT'])
@cross_origin(origin="*", headers=["Content-Type"])
def restart_game():
    #Get the query parameters to get the game id
    params = request.args
    #Check the game id information is correct
    Utils.check_game_id(params, game_sessions)
    game:Game = game_sessions.get(params.get('game_id'))
    
    game.restartGame()
    return jsonify({'board' : game.get_board()})


@tctctoe_server.route("/delete-session", methods = ['DELETE'])
@cross_origin(origin="*", headers=["Content-Type"])
def delete_game_session():
    #Get the query parameters to get the game id
    params = request.args
    #Check the game id information is correct
    Utils.check_game_id(params, game_sessions)
    game:Game = game_sessions.get(params.get('game_id'))

    #Delete the game session specified
    game_id = params.get('game_id')
    del game_sessions[game_id]
    print(f"Game session {game_id} has been deleted")
    return jsonify({'board' : game.get_board()})


if __name__ == "__main__":
    tctctoe_server.run(host='0.0.0.0', port=8080)