import unittest
from service_api_impl.GameSessionServiceSQLiteImpl import GameSessionServiceSQLiteImpl


class GameSessionServiceSQLiteImplTest(unittest.TestCase):

    def setUp(self):
        self.gameSessionServiceSQLiteImpl = GameSessionServiceSQLiteImpl()

    def test_start_game_session(self):

        game_session_id = self.gameSessionServiceSQLiteImpl.start_game_session("world")

        game_session = self.gameSessionServiceSQLiteImpl.get_game_session(game_session_id)

        self.assertEqual(game_session_id, game_session.id)
        self.assertEqual("world", game_session.target_word)

    def test_record_guess__get_guesses_for_game_session(self):

        game_session_id = self.build_test_game_session_with_guesses()

        guesses = self.gameSessionServiceSQLiteImpl.get_guesses_for_game_session(game_session_id)

        guess1 = guesses[0]
        guess2 = guesses[1]

        self.assertEqual(game_session_id, guess1.game_session_id)
        self.assertEqual(1, guess1.guess_number)
        self.assertEqual("angel", guess1.guess_word)

        self.assertEqual(game_session_id, guess2.game_session_id)
        self.assertEqual(2, guess2.guess_number)
        self.assertEqual("juicy", guess2.guess_word)

    def test_count_number_guesses_for_game_session__number_remaining_guesses(self):

        game_session_id = self.build_test_game_session_with_guesses()
        self.assertEqual(2, self.gameSessionServiceSQLiteImpl.count_number_guesses_for_game_session(game_session_id))
        self.assertEqual(4, self.gameSessionServiceSQLiteImpl.number_remaining_guesses(game_session_id))

    def build_test_game_session_with_guesses(self):

        game_session_id = self.gameSessionServiceSQLiteImpl.start_game_session("hello")
        game_session = self.gameSessionServiceSQLiteImpl.get_game_session(game_session_id)

        self.gameSessionServiceSQLiteImpl.record_guess("angel", 1, game_session.id)
        self.gameSessionServiceSQLiteImpl.record_guess("juicy", 2, game_session.id)

        return game_session_id










if __name__ == '__main__':
    unittest.main()
