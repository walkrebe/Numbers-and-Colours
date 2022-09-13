"""
Please refer to colours.txt which lists three colours per line

Using the same approach as for the numbers exercise, answer the following questions:

1. Which colour appears most in the file?
2. Which colour appears in the fewest number of lines
3. How many lines contain GREEN but not BLUE
4. How many lines have the same colour repeated three times?
5. How many lines have three different colours present?

Bonus Question

6. How many lines contain at least one colour pair in alphabetic order? For example,BLACK,YELLOW is an
alphabetically ordered pair, whereas ORANGE, BROWN is not
"""

from collections import Counter


class ReadFile:

    def __init__(self, filename: str, mode: str):
        self.filename = filename
        self.mode = mode

    def read(self):
        try:
            with open(self.filename, self.mode) as _file:
                for line in _file:
                    # remove blank lines
                    if not line.strip(): continue
                    # each line as a list of strings
                    yield line.strip().split(",")
        except IOError as e:
            msg = f"Can’t find file: {self.filename}"
            raise IOError(msg, e)


class Colours(ReadFile):

    def __init__(self, filename, mode):
        super().__init__(filename, mode)
        self.colour_total = Counter()
        self.lines_total = Counter()
        self.green_blue = 0
        self.alpha_order = 0
        self.same_colours = 0
        self.unique_colours = 0

    def most_common_colour(self):
        """Returns name of colour which appears the most """
        for line in self.read():
            self.colour_total.update(line)
        return self.colour_total.most_common(1)[0][0]

    def get_colour_fewest_lines(self):
        """Returns name of colour which appears in the fewest number of lines """
        for line in self.read():
            self.lines_total.update(set(line))
        return self.lines_total.most_common()[-1][0]

    def get_green_not_blue(self):
        for line in self.read():
            if "GREEN" in line and "BLUE" not in line:
                self.green_blue += 1
        return self.green_blue

    def count_lines_repeated_colours(self):
        for line in self.read():
            if line.count(line[0]) == len(line) and line:
                self.same_colours += 1
        return self.same_colours

    def count_lines_unique_colours(self):
        for line in self.read():
            if len(set(line)) == len(line):
                self.unique_colours += 1
        return self.unique_colours

    def get_alphabetical(self):
        for line in self.read():
            # Assume any colours starting with the same letter are alphabetical
            if any(a <= b for a, b in zip(line, line[1:])):
                self.alpha_order += 1
        return self.alpha_order


if __name__ == "__main__":
    colours = Colours('colours.txt', 'r')
    print(f"Most common colour: {colours.most_common_colour()}")
    print(f"{colours.get_colour_fewest_lines()} appears in the fewest number of lines")
    print(f"{colours.get_green_not_blue()} lines contain green but not blue")
    print(f"{colours.count_lines_repeated_colours()} lines where the colour is the same")
    print(f"{colours.count_lines_unique_colours()} lines where the colours are all unique")
    print(f"{colours.get_alphabetical()} lines contain at least one colour pair in alphabetical order")
