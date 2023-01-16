import unittest
from service.GameSessionService import GameSessionService
from service_api_impl.GameSessionRepositoryServiceSQLiteImpl import GameSessionRepositoryServiceSQLiteImpl
from main.constants import GuessStatusEnum


class GameSessionServiceTest(unittest.TestCase):

    def setUp(self):
        self.gameSessionService = GameSessionService()
        self.gameSessionRepositoryServiceSQLiteImpl = GameSessionRepositoryServiceSQLiteImpl()

    def test_take_a_guess_correct_first_try(self):

        target_word = "hello"
        game_session_id = self.gameSessionRepositoryServiceSQLiteImpl.create_game_session(target_word)
        guess_response = self.gameSessionService.take_a_guess("hello", game_session_id)
        self.assertEquals(GuessStatusEnum.correct, guess_response.guess_result)
        self.assertTrue(guess_response.game_over)

    def test_take_a_guess_all_incorrect_until_game_over(self):

        target_word = "hello"
        guess_words = ["goods", "cabal", "daily", "alure", "koala", "rhino"]
        game_session_id = self.gameSessionRepositoryServiceSQLiteImpl.create_game_session(target_word)

        for idx, guess_word in enumerate(guess_words):
            guess_response = self.gameSessionService.take_a_guess(guess_word, game_session_id)
            self.assertEquals(GuessStatusEnum.incorrect, guess_response.guess_result)
            if idx == 5:
                self.assertTrue(guess_response.game_over)
            else:
                self.assertFalse(guess_response.game_over)

    def test_take_a_guess_few_incorrect_one_correct(self):

        target_word = "hello"
        guess_words = ["goods", "cabal", "hello"]
        game_session_id = self.gameSessionRepositoryServiceSQLiteImpl.create_game_session(target_word)

        for idx, guess_word in enumerate(guess_words):
            guess_response = self.gameSessionService.take_a_guess(guess_word, game_session_id)
            if idx == 2:
                self.assertEquals(GuessStatusEnum.correct, guess_response.guess_result)
                self.assertTrue(guess_response.game_over)
            else:
                self.assertEquals(GuessStatusEnum.incorrect, guess_response.guess_result)
                self.assertFalse(guess_response.game_over)


if __name__ == '__main__':
    unittest.main()
