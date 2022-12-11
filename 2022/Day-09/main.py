"""
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2022
Description: This program implements my solution to the Advent of Code
 challenge.
"""

from rope import Rope


def main():
    """Main function to resolve the challenge."""

    directions = parse_data()

    print("\nPart one:")

    rope_one = Rope(length=2)
    rope_one.follow(directions)
    part_one_solution = len(rope_one.tail.unique_positions())

    print("  The number of unique positions is:", part_one_solution)

    print("\nPart two:")

    rope_two = Rope(length=10)
    rope_two.follow(directions)
    part_two_solution = len(rope_two.tail.unique_positions())

    print("  The number of unique positions is:", part_two_solution)


def parse_data():
    """Function to parse the input data of the challenge."""

    input_file = input("\nInput file: ")

    with open(input_file, 'r', encoding="utf-8") as infile:
        raw_data = infile.read().split("\n")

    if raw_data[-1] == "":
        raw_data.pop()

    raw_directions = [line.split(" ") for line in raw_data]
    directions = [(line[0], int(line[1])) for line in raw_directions]

    return directions


if __name__ == "__main__":
    main()
