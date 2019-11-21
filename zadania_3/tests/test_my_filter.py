import unittest

from zadania_3.my_solution.my_filter import my_filter


class TestMyFilter(unittest.TestCase):

    def test_gt_zero(self):
        test_list = [-3, -2, -1, 0, 1, 2, 3]
        func = lambda x: x > 0
        self.assertEqual(my_filter(func, test_list), [1, 2, 3])

    def test_empty_list(self):
        test_list = []
        func = lambda x: x > 0
        self.assertEqual(my_filter(func, test_list), [])

    def test_upper_letters(self):
        test_list = ['Ania', 'ala', 'Kasia', 'ola']
        func = lambda x: x[0].isupper()
        self.assertEqual(my_filter(func, test_list), ['Ania', 'Kasia'])

    def test_len_gt_five(self):
        test_list = ['Ala', 'Elzbieta', 'Kalinka', 'Kasia']
        func = lambda x: len(x) > 5
        self.assertEqual(my_filter(func, test_list), ['Elzbieta', 'Kalinka'])




if __name__ == '__main__':
    unittest.main()