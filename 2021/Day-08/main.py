'''
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2021
Description: This program implemets my solution to the Advent of Code challenge.
'''


def main():
    '''Main function to resolve the challenge.'''
    notes = parse_data()

    result = count_1_4_7_or_8_ocurrences(notes)

    print("\nThe number of times that '1', '4', '7', or '8' appear is:", result)


def parse_data():
    '''Funcion to parse the input data of the challenge.'''
    input_file = input("\nInput file: ")
    data = open(input_file, 'r').read().split("\n")

    if data[len(data) - 1] == '':
        data.pop()

    return [[part.split() for part in line.split(" | ")] for line in data]


def count_1_4_7_or_8_ocurrences(notes):
    '''Function to count how many times '1', '4', '7', or '8' appear in the
    output values.'''
    return sum([
        len(pattern) == 2 or \
        len(pattern) == 3 or \
        len(pattern) == 4 or \
        len(pattern) == 7 \
        for line in notes
        for pattern in line[1]
    ])


if __name__ == "__main__":
    main()
