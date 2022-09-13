import unittest
from colours_mg import Colours


class TestColours(unittest.TestCase):
    def test_count_lines_repeated_colours(self):
        self.assertEqual(Colours("test_colours.txt", "r").count_lines_repeated_colours(), 0)

    def test_count_lines_unique_colours(self):
        self.assertEqual(Colours("test_colours.txt", "r").count_lines_unique_colours(), 4)

    def test_get_alphabetical(self):
        self.assertEqual(Colours("test_colours.txt", 'r').get_alphabetical(), 4)

    def test_most_common_colour(self):
        self.assertEqual(Colours("test_colours.txt", 'r').most_common_colour(), 'GREEN')

    def test_get_colour_fewest_lines(self):
        self.assertEqual(Colours("test_colours.txt", 'r').get_colour_fewest_lines(), 'BLUE')

    def test_get_green_not_blue(self):
        self.assertEqual(Colours("test_colours.txt", 'r').get_green_not_blue(), 3)


if __name__ == '__main__':
    unittest.main()