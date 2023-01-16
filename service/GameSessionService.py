from service_api_impl.DictionaryServiceEnglishImpl import DictionaryServiceEnglishImpl
from service.WordleService import WordleService
from service_api_impl.GameSessionRepositoryServiceSQLiteImpl import GameSessionRepositoryServiceSQLiteImpl
from dto.web.GuessResponse import GuessResponse
from dto.web.NewGameResponse import NewGameResponse
from main import config


class GameSessionService:

    def __init__(self):
        self.dictionaryService = DictionaryServiceEnglishImpl()
        self.wordleService = WordleService()
        self.gameSessionRepositoryService = GameSessionRepositoryServiceSQLiteImpl()

    def new_game(self):

        target_word = self.dictionaryService.draw_random_word()
        game_session_id = self.gameSessionRepositoryService.create_game_session(target_word)
        print(f'Target Word: {target_word} for game_session_id: {game_session_id}')
        return NewGameResponse(game_session_id)

    def take_a_guess(self, guess_word, game_session_id):

        game_session = self.gameSessionRepositoryService.get_game_session(game_session_id)

        if self.is_game_over(game_session_id, game_session.target_word):
            guess_response = GuessResponse()
            guess_response.game_over = True
            guess_response.correct_word = game_session.target_word
            return guess_response

        guess_response = self.wordleService.guess(guess_word, game_session.target_word)

        self.gameSessionRepositoryService.record_guess(guess_word, game_session_id)

        guess_response.game_over = self.is_game_over(game_session_id, game_session.target_word)
        guess_response.correct_word = game_session.target_word if guess_response.game_over else None

        return guess_response

    def is_game_over(self, game_session_id, target_word):

        guesses = self.gameSessionRepositoryService.get_guesses_for_game_session(game_session_id)

        # if number of guesses made equals NUM_ALLOWED_GUESSES - game over
        if config.NUM_ALLOWED_GUESSES == len(guesses):
            return True

        # else if last guess is the target word - game over
        if len(guesses) > 0 and guesses[-1].guess_word == target_word:
            return True

        return False

