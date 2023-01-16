import requests, json, sys
from main.constants import GuessStatusEnum

if __name__ == '__main__':

    print("Example usage: python wordle_simulation_client.py {target_host} {target_port}.")
    print("if {target_host} and/or {target_port} are not specified, the defaults are localhost and 4637")

    # if target_host is not passed on command line, use localhost
    target_host = 'localhost' if len(sys.argv) <= 1 else sys.argv[1]
    target_port = 4637 if len(sys.argv) <= 2 else sys.argv[2]

    new_game_http_response = requests.post(f'http://{target_host}:{target_port}/new_game')
    new_game_response = new_game_http_response.json()

    game_id = new_game_response["game_id"]

    guess_words = ['alure', 'broke', 'lilac', 'curly', 'spine', 'hello', 'world']

    print(f'Game {game_id} started.')

    for guess_index, guess_word in enumerate(guess_words):
        body_json = {"game_id": game_id, "word": guess_word}
        guess_http_response = requests.post(f'http://{target_host}:{target_port}/guess', json=body_json)

        response = guess_http_response.json()
        assert GuessStatusEnum.incorrect == response["guess_result"]

        if guess_index + 1 >= 6:
            assert response["game_over"] is True
        else:
            assert response["game_over"] is False

        pretty_json = json.loads(guess_http_response.text)
        print(json.dumps(pretty_json, indent=2))
        print('------')

