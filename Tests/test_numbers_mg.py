import unittest
from numbers_mg import find_missing_number, find_most_common_digit


class TestNumbers(unittest.TestCase):
    def test_missing_numbers(self):
        self.assertEqual(find_missing_number("test_numbers.txt"), 15)

    def test_find_most_common_digit(self):
        self.assertEqual(find_most_common_digit("test_numbers.txt"), [('1', 10)])
