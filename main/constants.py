from enum import Enum


class GuessStatusEnum(str, Enum):
    correct = "correct",
    incorrect = "incorrect",
    wrong_position = "wrong_position"


letter = "letter"
