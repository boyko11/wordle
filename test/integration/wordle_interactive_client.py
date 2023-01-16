import requests, json, sys
from main.constants import GuessStatusEnum

if __name__ == '__main__':

    print("Example usage: python wordle_simulation_client.py {target_url}.")
    print("if {target_url} is not specified, the default is localhost:4637")

    target_url = 'localhost:4637' if len(sys.argv) <= 1 else sys.argv[1]

    new_game_http_response = requests.post(f'http://{target_url}/new_game')
    new_game_response = new_game_http_response.json()

    game_id = new_game_response["game_id"]

    print(f'Game {game_id} started.')

    # 7 to make sure we still "game_over" True for excessive guess requests
    for guess_index in range(7):

        guess_word = input("Your wordle word guess, followed by <Enter>: ")

        body_json = {"game_id": game_id, "word": guess_word}
        guess_http_response = requests.post(f'http://{target_url}/guess', json=body_json)

        response = guess_http_response.json()

        pretty_json_response = json.loads(guess_http_response.text)
        pretty_json = json.dumps(pretty_json_response, indent=2)

        if GuessStatusEnum.correct == response["guess_result"]:
            print(f"Hey, nice! You correctly guessed: {response['correct_word']}")
            assert response["game_over"] is True
            print(pretty_json)
            break

        if guess_index + 1 >= 6:
            assert response["game_over"] is True

        print(pretty_json)
        print('------')

