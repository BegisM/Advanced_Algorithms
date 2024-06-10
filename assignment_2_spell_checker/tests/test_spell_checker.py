import unittest
from assignment_2_spell_checker.dictionary.naive import NaiveDictionary
from assignment_2_spell_checker.dictionary.bbst import BBSTDictionary
from assignment_2_spell_checker.dictionary.trie import TrieDictionary
from assignment_2_spell_checker.dictionary.hashmap import HashMapDictionary


class TestSpellChecker(unittest.TestCase):
    def setUp(self):
        self.dictionary_file = 'data/english_words.txt'
        self.text_file = 'data/2600-0.txt'

    def test_naive(self):
        naive_dict = NaiveDictionary()
        naive_dict.load(self.dictionary_file)
        misspelled_words = naive_dict.spell_check(self.text_file)
        self.assertIsInstance(misspelled_words, list)

    def test_bbst(self):
        bbst_dict = BBSTDictionary()
        bbst_dict.load(self.dictionary_file)
        misspelled_words = bbst_dict.spell_check(self.text_file)
        self.assertIsInstance(misspelled_words, list)

    def test_trie(self):
        trie_dict = TrieDictionary()
        trie_dict.load(self.dictionary_file)
        misspelled_words = trie_dict.spell_check(self.text_file)
        self.assertIsInstance(misspelled_words, list)

    def test_hashmap(self):
        hashmap_dict = HashMapDictionary()
        hashmap_dict.load(self.dictionary_file)
        misspelled_words = hashmap_dict.spell_check(self.text_file)
        self.assertIsInstance(misspelled_words, list)


if __name__ == '__main__':
    unittest.main()
