# REST API Wordle
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
   2. Maintain Session State information - ie, How for along the game session for a certain game_id is - how many tries are left in the session for a specific game_id.  
4. Rest Stuff - Flask handler for the HTTP Posts

## Installation

```bash
pip install -r requirements.txt
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

## License
Feel free to use anyway you like, as long as you don't kill any puppies. Cheers!