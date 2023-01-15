import unittest
from service.WordleService import WordleService
from dto.GuessResponse import GuessResponse
from dto.constants import CorrectIncorrectEnum


class WordleServiceTest(unittest.TestCase):

    def setUp(self):
        self.wordleService = WordleService()

    def test_guess_returns_correct_response(self):
        expected_guess_response = GuessResponse(CorrectIncorrectEnum.correct, CorrectIncorrectEnum.correct,
                                                CorrectIncorrectEnum.correct, CorrectIncorrectEnum.correct,
                                                CorrectIncorrectEnum.correct, CorrectIncorrectEnum.correct, [])

        actual_guess_response = self.wordleService.guess("mules", "mules")

        self.assertEqual(expected_guess_response, actual_guess_response)


if __name__ == '__main__':
    unittest.main()
