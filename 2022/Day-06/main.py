"""
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2022
Description: This program implements my solution to the Advent of Code
 challenge.
"""


def main():
    """Main function to resolve the challenge."""

    datastream = parse_data()

    print("\nPart one:")

    start_marker = get_start_marker(datastream)
    part_one_solution = datastream.index(start_marker) + len(start_marker)

    print("  The number of processed characters is:", part_one_solution)

    print("\nPart two:")

    start_marker = get_start_marker(datastream, start_marker_len=14)
    part_two_solution = datastream.index(start_marker) + len(start_marker)

    print("  The number of processed characters is:", part_two_solution)


def parse_data():
    """Function to parse the input data of the challenge."""

    input_file = input("\nInput file: ")

    with open(input_file, 'r', encoding="utf-8") as infile:
        raw_data = infile.read().split("\n")

    return raw_data[0]


def get_start_marker(datastream, start_marker_len=4):
    """Function to get the start marker."""

    for i in range(len(datastream) - start_marker_len):
        substring = datastream[i:i + start_marker_len]

        if len({*substring}) == start_marker_len:
            return substring


if __name__ == "__main__":
    main()
