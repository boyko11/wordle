from enum import Enum


class GuessStatusEnum(Enum):
    correct = "correct",
    incorrect = "incorrect",
    wrong_position = "wrong_position"


letter = "letter"

NUM_ALLOWED_GUESSES = 6
