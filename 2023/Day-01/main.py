"""
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2023
Description: This program implements my solution to the Advent of Code challenge.
"""


def main():
    """Main function to resolve the challenge."""

    encoded_calibration_document = parse_data()

    original_calibration_values = [
        recover_original_value(encoded_calibration_value)
        for encoded_calibration_value in encoded_calibration_document
    ]

    solution = sum(original_calibration_values)

    print("The sum of all original calibration values is:", solution)


def parse_data():
    """Function to parse the input data of the challenge."""

    input_file = input("\nInput file: ")

    with open(input_file, 'r', encoding="utf-8") as infile:
        rawdata = infile.read().split()

    return rawdata


def recover_original_value(encoded_calibration_value):
    """Function to recover the original value from the encoded one."""

    digits = [
        character
        for character in encoded_calibration_value
        if character.isdigit()
    ]

    original_calibration_value = int(digits[0] + digits[-1])

    return original_calibration_value


if __name__ == "__main__":
    main()
