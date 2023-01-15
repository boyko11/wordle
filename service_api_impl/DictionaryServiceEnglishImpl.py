from english_words import get_english_words_set
from random import randrange
from service_api.DictionaryService import DictionaryService


class DictionaryServiceEnglishImpl(DictionaryService):

    def __init__(self):
        self.five_letter_words = self.load_all_five_letter_words()

    def load_all_five_letter_words(self):
        web2_words_set = get_english_words_set(['web2'], lower=True)
        return [this_word for this_word in web2_words_set if len(this_word) == 5]

    def draw_random_word(self):
        return self.five_letter_words[randrange(len(self.five_letter_words))]