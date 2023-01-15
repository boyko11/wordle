import unittest
from service.WordleService import WordleService
from dto.GuessResponse import GuessResponse
from dto.constants import GuessStatusEnum


class WordleServiceTest(unittest.TestCase):

    def setUp(self):
        self.wordleService = WordleService()

    def test_guess_returns_correct_response(self):
        expected_guess_response = GuessResponse(GuessStatusEnum.correct, GuessStatusEnum.correct,
                                                GuessStatusEnum.correct, GuessStatusEnum.correct,
                                                GuessStatusEnum.correct, GuessStatusEnum.correct, [])

        actual_guess_response = self.wordleService.guess("mules", "mules")

        self.assertEqual(expected_guess_response, actual_guess_response)

    def test_get_correct_indices_some_correct(self):
        self.assertEqual([0, 1, 3, 4], self.wordleService.get_correct_indices("abcde", "abzde"))

    def test_get_correct_indices_all_incorrect(self):
        self.assertEqual([], self.wordleService.get_correct_indices("abcde", "fghij"))

    def test_get_incorrect_indices_some_incorrect(self):
        incorrect_or_wrong_position_indices = set([0, 2, 4])

        self.assertEqual(set([2, 4]), self.wordleService.get_incorrect_indices("abcde", "abzdf",
                                                                               incorrect_or_wrong_position_indices))

    def test_get_correct_indices_all_incorrect(self):
        incorrect_or_wrong_position_indices = set(range(5))
        self.assertEqual(set(range(5)), self.wordleService.get_incorrect_indices("abcde", "fghij",
                                                                                 incorrect_or_wrong_position_indices))

    def test_get_wrong_position_indices(self):
        incorrect_or_wrong_position_indices = set([0, 2, 4])
        incorrect_indices = set([2, 4])

        self.assertEqual(set([0]), self.wordleService.get_wrong_position_indices(incorrect_or_wrong_position_indices,
                                                                                 incorrect_indices))

    def test_build_incorrect_guess_response(self):
        # guess  "azure"
        # target "audio"

        correct_idx = [0]
        incorrect_idx = set([1, 3, 4])
        wrong_position_idx = set([2])

        actual_guess_response = self.wordleService.build_incorrect_guess_response(correct_idx, incorrect_idx,
                                                                                  wrong_position_idx, "azure")

        expected_guess_response = self.build_incorrect_test_guess_response()

        self.assertEqual(actual_guess_response, expected_guess_response)

    def test_guess_incorrect_response(self):
        expected_guess_response = self.build_incorrect_test_guess_response()

        actual_guess_response = self.wordleService.guess("azure", "audio")

        self.assertEqual(expected_guess_response, actual_guess_response)

    def test_guess_incorrect_response_duplicate_guess_letters(self):

        expected_guess_response = GuessResponse(GuessStatusEnum.incorrect,
                                                GuessStatusEnum.wrong_position,
                                                GuessStatusEnum.correct,
                                                GuessStatusEnum.incorrect,
                                                GuessStatusEnum.wrong_position,
                                                GuessStatusEnum.wrong_position,
                                                ["c"])

        actual_guess_response = self.wordleService.guess("local", "koala")

        self.assertEqual(expected_guess_response, actual_guess_response)

    def build_incorrect_test_guess_response(self):
        return GuessResponse(GuessStatusEnum.incorrect,
                             GuessStatusEnum.correct,
                             GuessStatusEnum.incorrect,
                             GuessStatusEnum.wrong_position,
                             GuessStatusEnum.incorrect,
                             GuessStatusEnum.incorrect,
                             ["z", "r", "e"])


if __name__ == '__main__':
    unittest.main()
