from dataclasses import dataclass

@dataclass
class GuessResponse:
    guess_result: str
    letter1: str
    letter2: str
    letter3: str
    letter4: str
    letter5: str
    incorrectly_guessed_letters: list

