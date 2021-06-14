import unittest

from main import init_list, diff_list, min_coin_swap


class TestMain(unittest.TestCase):

    def test_init_list_size_3(self):
        self.assertEqual(init_list(3), ([0, 1, 0], [1, 0, 1]))

    def test_init_list_size_5(self):
        self.assertEqual(init_list(5), ([0, 1, 0, 1, 0], [1, 0, 1, 0, 1]))

    def test_init_list_size_8(self):
        self.assertEqual(init_list(8), ([0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0]))

    def test_diff_list_opposite_size_5(self):
        self.assertEqual(diff_list(*init_list(5)), 5)

    def test_diff_list_start_with_zero(self):
        self.assertEqual(diff_list([1, 1, 0, 1, 0, 1, 1], [0, 1, 0, 1, 0, 1, 0]), 2)

    def test_diff_list_start_with_one(self):
        self.assertEqual(diff_list([1, 1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 1, 0, 1]), 5)

    def test_min_coin_swap_invalid_input(self):
        with self.assertRaises(ValueError):
            min_coin_swap([1, 0, 1, 2])

    def test_min_coin_swap_list_one(self):
        self.assertEqual(min_coin_swap([1, 1, 0, 0, 1, 0, 1]), 2)

    def test_min_coin_swap_list_two(self):
        self.assertEqual(min_coin_swap([1, 1, 0, 1, 0, 1, 1]), 2)
