"""
Please refer to numbers.txt which contains 1562 lines, each with a number between 1 and
1563. Each number appears at most once, and one is missing from the sequence.

Please answer the following questions, either by writing a script (any language) to determine the exact answer, or pseudo-code/ a decision tree
to illustrate the approach/algorithm you would use to solve:
1. Which digit appears most in the file
2. Which number is missing

"""

from collections import Counter


def read_file(filename):
    try:
        with open(filename, 'r') as _file:
            for line in _file:
                yield line.rstrip()
    except IOError as e:
        msg = f"Can’t find file: {filename}"
        raise IOError(msg, e)


def find_missing_number(filename: str) -> int:
    """
        :param filename: File being read from
        :return: The number which is missing in the range. As numbers are distinct, subtract sum of all numbers from
        (n)n+1/2 where n is last number in the range (in the example n=1563).
    """
    no_of_lines = 0
    sum_numbers = 0
    for line in read_file(filename):
        no_of_lines += 1
        if line.isalnum():
            sum_numbers += int(line)
    missing_num = ((no_of_lines + 1) * (no_of_lines + 2) // 2) - sum_numbers
    return missing_num


def find_most_common_digit(filename: str) -> list[tuple]:
    """ Returns most common digit(s) and corresponding frequency """
    total_digits = Counter()
    for line in read_file(filename):
        if line.isalnum():
            total_digits.update(line)
    max_digit_count = total_digits.most_common()[0][1]
    # Get those digits that occur at the max frequency
    most_common = [(digit, count) for digit, count in total_digits.items() if count == max_digit_count]
    return most_common


if __name__ == '__main__':
    filename = 'numbers.txt'
    print(f"The missing number is: {find_missing_number('numbers.txt')}")
    print('\n '.join([f'Most Common Digit: {str(x[0])}' + ' ' + f"Occurrence: {str(x[1])}" for x in
                      find_most_common_digit('numbers.txt')]))
