import unittest

from zadania_3.my_solution.szyfr_cezara import szyfruj_cezar


class TestCaesarCipher(unittest.TestCase):

    def test_empty_string(self):
        test_string = ''
        self.assertEqual(szyfruj_cezar(test_string), '')

    def test_first_string(self):
        test_string = 'ABC DEF GHI'
        self.assertEqual(szyfruj_cezar(test_string), 'DEF GHI JKL')

    def test_comma(self):
        test_string = ', , ,'
        self.assertEqual(szyfruj_cezar(test_string), ', , ,')


if __name__ == '__main__':
    unittest.main()
