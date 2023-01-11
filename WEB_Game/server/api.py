from flask import Flask, request, jsonify, abort
from flask_cors import CORS, cross_origin
import json
from GL.Game import Game

app = Flask(__name__)
#Adding CORS for the app
CORS(app)
game = Game()

@app.route('/get-board', methods = ['GET'])
@cross_origin(origin="*", headers=["Content-Type"])
def get_board():
    return jsonify({'board' : game.get_board()})

@app.route('/winner', methods = ['GET'])
@cross_origin(origin="*", headers=["Content-Type"])
def get_winner():
    winner = game.winner
    if game.numbers_In_Board == 0:
        winner = "tie"
    return jsonify({'winner' : winner})

@app.route('/move', methods = ['POST'])
@cross_origin(origin="*", headers=["Content-Type"])
def user_move():
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

@app.route('/machine-move', methods = ['GET'])
@cross_origin(origin="*", headers=["Content-Type"])
def machine_move():
    game.machineMove()
    game.victory()
    return jsonify({'board' : game.get_board()})

@app.route("/restart", methods = ['PUT'])
@cross_origin(origin="*", headers=["Content-Type"])
def restart_game():
    game.restartGame()
    return jsonify({'board' : game.get_board()})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)