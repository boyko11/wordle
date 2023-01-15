from dto.constants import CorrectIncorrectEnum
from dto.GuessResponse import GuessResponse


class WordleService:

    def __init__(self):
        pass

    def guess(self, guess_word, target_word):

        if guess_word == target_word:
            return GuessResponse(CorrectIncorrectEnum.correct, CorrectIncorrectEnum.correct,
                                 CorrectIncorrectEnum.correct, CorrectIncorrectEnum.correct,
                                 CorrectIncorrectEnum.correct, CorrectIncorrectEnum.correct, [])

        return None