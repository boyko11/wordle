# REST API Wordle
## Quick Blurb
This wordle clone API is not as robust as it could be.  
Specifically, it could use http request validation,  
nicer handling of guess attempts after the max allowed guesses,  
more robust wordle rules, dictionary that does not contain impossible words.  
If the intent was to demonstrate more robustness on these points, let me know. Cheers!

## Test instructions
### 1. Local No Docker
Clone the project locally and cd to the project dir.
Get all the libraries:  
```bash
pip install -r requirements.txt
```
Start Flask locally
```bash
python -m main.web
```
The flask terminal window will print the correct target word when a new game starts.  

cd to the project root in different terminal window or a tab.  
Run a simulation - it starts a game and makes 7 incorrect guesses.  
It asserts that the 6th and any following guess attempts, return "game_over"
```bash
python -m test.integration.wordle_simulation_client
```
This will go after localhost:4637. If you want different host and/or port

```bash
python -m test.integration.wordle_simulation_client {target_host} {target_port}
```

Interactive command-line wordle client:  
From the project root dir  
```bash
python -m test.integration.wordle_interactive_client
```
Again localhost:4637 is the default, if different desired:
```bash
python -m test.integration.wordle_interactive_client {target_host} {target_port}
```





## Requirements
To start a game session, HTTP Post with an empty body to  
**/new_game**  
The return will be the game_id to be referenced during the game session, e.g.
```json
{
  "game_id": 123456
}
```

To make a guess HTTP Post the guess word to  
**/guess**  
with following example body:
```json
{
    "game_id": 123456, 
    "word": "CROWN"
}
```
The return to this post request would be the result of the guess, e.g.
```json
{
    "guess_result": "incorrect",
    "letter1": "incorrect", 
    "letter2": "correct", 
    "letter3": "wrong_position", 
    "letter4": "incorrect", 
    "letter5": "incorrect", 
    "incorrectly_guessed_letters": ["C", "W", "N"]
}
```

## Design blurb

1. DictionaryService
   1. Load all five-letter english words - just once at program start-up
   2. Draw a random five-letter word
2. WordleGuessService - given a guess word and a target word return the guess response as described in the requirements
3. GameSessionService
   1. Start a game session - generate a unique GameSessionId
   2. Maintain Session State information - Record guesses. Have them available in case of backend restart. Indicate game over
4. Rest Stuff - Flask handler for the HTTP Posts

## Installation

```bash
pip install -r docker/requirements.txt
```

## Usage

Build as docker flask container from the project root dir(not from the docker subdir)
```bash
docker build . -t wordle:latest -f docker/Dockerfile
```

Then run on whatever port you like:
```bash
docker run -p 8000:4637 -d wordle
```

Then HTTP post wuth an empty body to
```http request
http://localhost:8000/new_game
```
Example response:
```json
{
  "game_id": 123456
}
```

Then get the game_id from the response and HTTP Post a "guess"
```http request
http://localhost:8000/new_game
```
Example body:
```json
{
    "game_id": 123456, 
    "word": "CROWN"
}
```


## License
Feel free to use anyway you like, as long as you mean no harm. Cheers!