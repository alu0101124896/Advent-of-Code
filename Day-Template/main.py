"""
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: # ToDo: Add date
Description: This program implements my solution to the Advent of Code challenge.
"""


def main():
    """Main function to resolve the challenge."""

    parsed_data = parse_data()

    solution = main_challenge_function()

    print("The solution", solution)


def parse_data():
    """Function to parse the input data of the challenge."""

    input_file = input("\nInput file: ")

    with open(input_file, 'r', encoding="utf-8") as infile:
        rawdata = infile.read().split()

    parsed_data = None  # ToDo: Add data parsing

    return parsed_data


def main_challenge_function():
    """Function to # ToDo: Add function info."""

    solution = None  # ToDo: Add function functionality

    return solution


if __name__ == "__main__":
    main()
