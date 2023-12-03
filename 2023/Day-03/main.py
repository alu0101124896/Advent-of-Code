"""
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2023
Description: This program implements my solution to the Advent of Code challenge.
"""

import re


def main():
    """Main function to resolve the challenge."""

    engine_schematic = parse_data()

    part_numbers = get_part_numbers(engine_schematic)

    print("The sum of all part numbers is:", sum(part_numbers))


def parse_data():
    """Function to parse the input data of the challenge."""

    input_file = input("\nInput file: ")

    with open(input_file, "r", encoding="utf-8") as infile:
        rawdata = infile.read().split("\n")

    if rawdata[-1] == "":
        rawdata.pop(-1)

    engine_schematic = {
        "visual_representation": rawdata,
        "symbols": [],
    }

    for line_index, line_data in enumerate(rawdata):
        for symbol in re.finditer(r"[^\d.]", line_data):
            engine_schematic["symbols"].append(
                {
                    "symbol": symbol.group(),
                    "line": line_index,
                    "column": symbol.start(),
                }
            )

    return engine_schematic


def get_part_numbers(engine_schematic):
    """Function to get the part numbers from the engine schematic. The part numbers are
    the numbers that are adjacent to a symbol."""

    part_numbers = []

    for symbol in engine_schematic["symbols"]:
        for line in engine_schematic["visual_representation"][
            (symbol["line"] - 1) : (symbol["line"] + 2)
        ]:
            for number in re.finditer(r"\d+", line):
                if (
                    number.start() <= symbol["column"] + 1
                    and number.end() - 1 >= symbol["column"] - 1
                ):
                    part_numbers.append(int(number.group()))

    return part_numbers


if __name__ == "__main__":
    main()
