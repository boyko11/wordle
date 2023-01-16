from dataclasses import dataclass


@dataclass
class GameSessionGuess:

    game_session_id: int
    guess_number: int
    guess_word: str
