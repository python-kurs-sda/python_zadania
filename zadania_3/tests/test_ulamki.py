import unittest

from zadania_3.my_solution.ulamki import Fraction


class TestFraction(unittest.TestCase):

    def test_fraction_init(self):
        fract = Fraction(1 , 2)
        self.assertEqual(fract.nominator, 1)
        self.assertEqual(fract.denominator, 2)

    def test_add_common_denominator(self):
        fract1 = Fraction(1, 5)
        fract2 = Fraction(2, 5)
        result = fract1 + fract2
        self.assertEqual(result.nominator, 3)

    def test_add_different_denominator(self):
        fract1 = Fraction(1, 5)
        fract2 = Fraction(2, 3)
        result = fract1 + fract2
        self.assertEqual(result.nominator, 13)
        self.assertEqual(result.denominator, 15)

    def test_add_three_fraction_common_denominator(self):
        fract1 = Fraction(1, 5)
        fract2 = Fraction(2, 5)
        fract3 = Fraction(1, 5)
        result = fract1 + fract2 + fract3
        self.assertEqual(result.nominator, 4)
        self.assertEqual(result.denominator, 5)

    def test_add_three_fraction_different_denominator(self):
        fract1 = Fraction(1, 2)
        fract2 = Fraction(2, 5)
        fract3 = Fraction(1, 3)
        result = fract1 + fract2 + fract3
        self.assertEqual(result.nominator, 37)
        self.assertEqual(result.denominator, 30)

    def test_sub_common_denominator(self):
        fract1 = Fraction(3, 5)
        fract2 = Fraction(1, 5)
        result = fract1 - fract2
        self.assertEqual(result.nominator, 2)
        self.assertEqual(result.denominator, 5)

    def test_sub_different_denominator(self):
        fract1 = Fraction(3, 5)
        fract2 = Fraction(1, 6)
        result = fract1 - fract2
        self.assertEqual(result.nominator, 13)
        self.assertEqual(result.denominator, 30)

    def test_mul(self):
        fract1 = Fraction(3, 5)
        fract2 = Fraction(1, 6)
        result = fract1 * fract2
        self.assertEqual(result.nominator, 3)
        self.assertEqual(result.denominator, 30)

    def test_truediv(self):
        fract1 = Fraction(3, 5)
        fract2 = Fraction(1, 6)
        result = fract1 / fract2
        self.assertEqual(result.nominator, 18)
        self.assertEqual(result.denominator, 5)


if __name__ == '__main__':
    unittest.main()