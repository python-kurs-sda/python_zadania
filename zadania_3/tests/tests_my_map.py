import unittest

from zadania_3.my_solution.my_map import my_map


class TestMyMap(unittest.TestCase):

    def test_with_add_one(self):
        my_list = [1, 2, 3, 4]
        func = lambda x: x + 1
        self.assertEqual(my_map(func, my_list), [2, 3, 4, 5])

    def test_with_multi_by_two(self):
        my_list = [1, 2, 3, 4]
        func = lambda x: x * 2
        self.assertEqual(my_map(func, my_list), [2, 4, 6, 8])


if __name__ == '__main__':
    unittest.main()
