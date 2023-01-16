import unittest
from service_api_impl.DictionaryServiceEnglishImpl import DictionaryServiceEnglishImpl


class DictionaryServiceEnglishImplTest(unittest.TestCase):

    def setUp(self):
        self.dictionaryServiceEnglishImpl = DictionaryServiceEnglishImpl()

    def test_load_five_letter_words_should_return_five_letter_words(self):
        five_letter_words = self.dictionaryServiceEnglishImpl.load_all_five_letter_words()
        self.assertTrue(all([len(this_word) == 5 for this_word in five_letter_words]),
                        "Expected All Words to be of length 5.")

    def test_draw_random_word_draws_random_five_letter_word(self):

        random_words_sample = []
        for i in range(100):
            random_words_sample.append(self.dictionaryServiceEnglishImpl.draw_random_word())

        self.assertTrue(all([len(this_word) == 5 for this_word in random_words_sample]),
                        "Expected all Words to be of length 5.")

        # some leeway for the rare chance some words were drawn twice
        self.assertTrue(len(set(random_words_sample)) > 95,
                        "Expected the words to be random - max of 5 duplicates.")


if __name__ == '__main__':
    unittest.main()
