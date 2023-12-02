"""
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2023
Description: This program implements my solution to the Advent of Code challenge.
"""

import re


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

    valid_digits = r"\d|one|two|three|four|five|six|seven|eight|nine"

    first_digit = re.match(
        rf".*?(?P<first_digit>{valid_digits}).*",
        encoded_calibration_value,
    ).group("first_digit")

    last_digit = re.match(
        rf".*(?P<last_digit>{valid_digits}).*?",
        encoded_calibration_value,
    ).group("last_digit")

    original_calibration_value = int(
        digitize_digit(first_digit)
        + digitize_digit(last_digit)
    )

    return original_calibration_value


def digitize_digit(number):
    """Function to digitize a number."""

    if number.isdigit():
        return number

    elif number == "one":
        return "1"
    elif number == "two":
        return "2"
    elif number == "three":
        return "3"
    elif number == "four":
        return "4"
    elif number == "five":
        return "5"
    elif number == "six":
        return "6"
    elif number == "seven":
        return "7"
    elif number == "eight":
        return "8"
    elif number == "nine":
        return "9"

    else:
        raise ValueError


if __name__ == "__main__":
    main()
