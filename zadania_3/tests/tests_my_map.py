import unittest

from zadania_3.my_solution.my_map import my_map


class TestMyMap(unittest.TestCase):

    def test_with_add_one(self):
        test_list = [1, 2, 3, 4]
        func = lambda x: x + 1
        self.assertEqual(my_map(func, test_list), [2, 3, 4, 5])

    def test_with_multi_by_two(self):
        test_list = [1, 2, 3, 4]
        func = lambda x: x * 2
        self.assertEqual(my_map(func, test_list), [2, 4, 6, 8])

    def test_multi_string(self):
        test_list = ['ab', 'cd', 'ef', 'gh']
        func = lambda x: x * 2
        self.assertEqual(my_map(func, test_list), ['abab', 'cdcd', 'efef', 'ghgh'])

    def test_upper_letter(self):
        test_list = ['ala', 'ola', 'iza']
        func = lambda x: x.upper()
        self.assertEqual(my_map(func, test_list), ['ALA', 'OLA', 'IZA'])

    

if __name__ == '__main__':
    unittest.main()
