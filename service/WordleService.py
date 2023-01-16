from main import constants
from main.constants import GuessStatusEnum
from dto.GuessResponse import GuessResponse


class WordleService:

    def __init__(self):
        pass

    def guess(self, guess_word, target_word):

        if guess_word == target_word:
            return GuessResponse(GuessStatusEnum.correct, GuessStatusEnum.correct,
                                 GuessStatusEnum.correct, GuessStatusEnum.correct,
                                 GuessStatusEnum.correct, GuessStatusEnum.correct, [])

        correct_indices = self.get_correct_indices(guess_word, target_word)
        incorrect_or_wrong_position_indices = set(range(len(target_word))) - set(correct_indices)

        # remaining indices are either incorrect or wrong position
        incorrect_indices = self.get_incorrect_indices(guess_word, target_word, incorrect_or_wrong_position_indices)

        wrong_position_indices = self.get_wrong_position_indices(incorrect_or_wrong_position_indices, incorrect_indices)

        return self.build_incorrect_guess_response(correct_indices, incorrect_indices, wrong_position_indices, guess_word)

    def get_correct_indices(self, guess_word, target_word):
        # Find letters in correct positions:
        # Create a list of two-tuples (same_index_guess_word, same_index_target_word) - zip(guess_word, target_word)
        # Then if any tuple consists of identical chars, the guess for this index is correct

        return [index for index, letters_pair in enumerate(zip(guess_word, target_word))
                if len(set(letters_pair)) == 1]

    def get_incorrect_indices(self, guess_word, target_word, incorrect_or_wrong_position_indices):

        # use case 1: letter in guess is NOT in target => incorrect
        incorrect_indices = [idx for idx in incorrect_or_wrong_position_indices if guess_word[idx] not in target_word]

        # we can get creative with the edge cases
        # but there does not seem to be an official wordle rules standard for multiple occurrence letters
        # I have seen a guess word with multiple letters - local, mark only the first occurrence of 'l' as wrong
        # position, but the second one as incorrect.
        # this implementation just marks it as a wrong_position
        # Will keep it simple for now, but will ask for feedback if more robust rules are expected

        return set(incorrect_indices)

    def get_wrong_position_indices(self, incorrect_or_wrong_position_indices, incorrect_indices):

        return incorrect_or_wrong_position_indices - incorrect_indices

    def build_incorrect_guess_response(self, correct_indices, incorrect_indices, wrong_position_indices, guess_word):

        guess_response = GuessResponse()
        guess_response.guess_result = GuessStatusEnum.incorrect
        guess_response.incorrectly_guessed_letters = [guess_word[idx] for idx in incorrect_indices]

        # plus one for each index to match the attribute name(0 translates to letter1)
        for idx in correct_indices:
            setattr(guess_response, constants.letter + str(idx + 1), GuessStatusEnum.correct)

        for idx in incorrect_indices:
            setattr(guess_response, constants.letter + str(idx + 1), GuessStatusEnum.incorrect)

        for idx in wrong_position_indices:
            setattr(guess_response, constants.letter + str(idx + 1), GuessStatusEnum.wrong_position)

        return guess_response
