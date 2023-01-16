# REST API Wordle
## Quick Blurb
This wordle clone API is not as robust as it could be.  
Specifically, it could use http request validation,  
nicer handling of guess attempts after the max allowed guesses,  
more robust wordle rules, dictionary that does not contain impossible words.  
If the intent was to demonstrate more robustness on these points, let me know. Cheers!

## Local Test instructions
Clone the project locally and cd to the project dir.
Get all the libraries:  
```bash
pip install -r requirements.txt
```
### 1. Docker

Build as docker flask container from the project root dir(not from the docker subdir)
```bash
docker build . -t wordle:latest -f docker/Dockerfile
```

Flask runs on port 4637, but you can run on whatever port you like:
```bash
docker run -p 4637:4637 -d wordle
```

### 2. NO docker

Start Flask locally
```bash
python -m main.web
```
The flask terminal window will print the correct target word when a new game starts.  

### Testing and simulation

cd to the project root in different terminal window or a tab.  
Run a simulation - it starts a game and makes 7 incorrect guesses.  
It asserts that the 6th and any following guess attempts, return "game_over"
```bash
python -m test.integration.wordle_simulation_client
```
This will go after localhost:4637. If you'd like a different target_url

```bash
python -m test.integration.wordle_simulation_client {target_url}
```

Interactive command-line wordle client:  
From the project root dir  
```bash
python -m test.integration.wordle_interactive_client
```
Again localhost:4637 is the default, if different desired:
```bash
python -m test.integration.wordle_interactive_client {target_url}
```

#### Postman
See postman dir under the project root.  
You could import the postman environment and collection json files into your Postman.  
It has a new_game post to localhost:4637, then grabs the game_id from the response  
and sets it as an env variable used for the following "guess" requests.

## Remote Test instructions
The docker container is also deployed on  
http://boyko.io/wordle
You could run the local test scripts from the project root dir, passing just the remote {target_url}:  
```bash
python -m test.integration.wordle_simulation_client boyko.io/wordle
```
```bash
python -m test.integration.wordle_interactice_client boyko.io/wordle
```

### Remote Postman
If you'd like to go after the remote boyko wordle with Postman, 
You could use the provided Postman project - just change the env variable "target_url" to be boyko.io/wordle 



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

## License
Feel free to use anyway you like, as long as you mean no harm. Cheers!