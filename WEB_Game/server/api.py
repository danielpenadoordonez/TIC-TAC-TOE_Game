from flask import Flask, request, jsonify, abort
import json
from GL.Game import Game

app = Flask(__name__)

game = Game()

@app.route('/', methods = ['GET'])
def get_board():
    return jsonify({'board' : game.get_board()})

@app.route('/winner', methods = ['GET'])
def get_winner():
    winner = game.winner
    if game.numbers_In_Board == 0:
        winner = "tie"
    return jsonify({'winner' : winner})

@app.route('/move', methods = ['POST'])
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
def machine_move():
    game.machineMove()
    game.victory()
    return jsonify({'board' : game.get_board()})

@app.route("/restart", methods = ['PUT'])
def restart_game():
    game.restartGame()

if __name__ == "__main__":
    app.run(port=8080)