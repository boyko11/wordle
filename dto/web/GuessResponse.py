from dataclasses import dataclass, field
from main.constants import GuessStatusEnum


@dataclass
class GuessResponse:
    guess_result: str = GuessStatusEnum.incorrect
    letter1: str = GuessStatusEnum.incorrect
    letter2: str = GuessStatusEnum.incorrect
    letter3: str = GuessStatusEnum.incorrect
    letter4: str = GuessStatusEnum.incorrect
    letter5: str = GuessStatusEnum.incorrect
    incorrectly_guessed_letters: list = field(default_factory=list)
    game_over: bool = False
    correct_word: str = None
