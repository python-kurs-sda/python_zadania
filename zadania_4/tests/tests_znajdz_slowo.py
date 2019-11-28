import unittest
from zadania_4.my_solution.znajdz_slowo import find_word, find_word_regex


class TestFindWord(unittest.TestCase):

    def test_first_signs(self):
        test_signs = '123456NAPIS7890'
        self.assertEqual(find_word(test_signs), 'NAPIS')

    def test_second_signs(self):
        test_signs = '000000kolejnynapis000000'
        self.assertEqual(find_word(test_signs), 'kolejnynapis')

    def test_third_signs(self):
        test_signs = 'innyNAPIS123456789'
        self.assertEqual(find_word(test_signs), 'innyNAPIS')

    def test_fourth_signs(self):
        test_signs = '123JESZCZEinnyNAPIS00'
        self.assertEqual(find_word(test_signs), 'JESZCZEinnyNAPIS')


class TestFindWordRegex(unittest.TestCase):

    def test_first_signs(self):
        test_signs = '123456NAPIS7890'
        self.assertEqual(find_word_regex(test_signs), 'NAPIS')

    def test_second_signs(self):
        test_signs = '000000kolejnynapis000000'
        self.assertEqual(find_word_regex(test_signs), 'kolejnynapis')

    def test_third_signs(self):
        test_signs = 'innyNAPIS123456789'
        self.assertEqual(find_word_regex(test_signs), 'innyNAPIS')

    def test_fourth_signs(self):
        test_signs = '123JESZCZEinnyNAPIS00'
        self.assertEqual(find_word_regex(test_signs), 'JESZCZEinnyNAPIS')


if __name__ == '__main__':
    unittest.main()