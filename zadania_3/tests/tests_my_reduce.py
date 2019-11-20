import unittest

from zadania_3.my_solution.my_reduce import my_reduce


class TestMyReduce(unittest.TestCase):

    def test_sum_of_elements(self):
        test_list = [1, 2, 3, 4]
        func = lambda x, y: x + y
        self.assertEqual(my_reduce(func, test_list), 10)

    def test_multi_of_elements(self):
        test_list = [1, 2, 3, 4]
        func = lambda x, y: x * y
        self.assertEqual(my_reduce(func, test_list), 24)

    def test_div_of_elements(self):
        test_list = [1, 2, 3, 4]
        func = lambda x, y: x / y
        self.assertAlmostEqual(my_reduce(func, test_list), 0.041666667)


if __name__ == '__main__':
    unittest.main()