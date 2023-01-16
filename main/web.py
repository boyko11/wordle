from flask import Flask, jsonify, request
from waitress import serve
from service.GameSessionService import GameSessionService


app = Flask(__name__)


@app.route('/', methods=['GET'])
def wordle_home():

    return "POST to /new_game to start a new game."


@app.route('/new_game', methods=['POST'])
def new_game():

    return jsonify(gameSessionService.new_game())


@app.route('/guess', methods=['POST'])
def guess():

    guess_request = request.json
    game_session_id = guess_request["game_id"]
    guess_word = guess_request["word"]

    return jsonify(gameSessionService.take_a_guess(guess_word, game_session_id))


if __name__ == "__main__":

    # import os
    # port = int(os.environ.get('PORT', 4637))
    # app.run(debug=True, host='0.0.0.0', port=port)

    gameSessionService = GameSessionService()

    serve(app, host="0.0.0.0", port=4637)