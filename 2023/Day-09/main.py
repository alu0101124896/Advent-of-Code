"""
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: August 2024
Description: This program implements my solution to the Advent of Code challenge.
"""


def main():
    """Main function to resolve the challenge."""

    sensor_report = parse_data()

    extrapolated_values = [
        extrapolate_next_value_record(value_history) for value_history in sensor_report
    ]

    print("The sum of all extrapolated values is", sum(extrapolated_values))


def parse_data():
    """Function to parse the input data of the challenge."""

    input_file = input("\nInput file: ")

    with open(input_file, "r", encoding="utf-8") as infile:
        rawdata = infile.read().split("\n")

    if rawdata[-1] == "":
        rawdata.pop(-1)

    sensor_report = [
        [int(value_record) for value_record in value_history.split()]
        for value_history in rawdata
    ]

    return sensor_report


def extrapolate_next_value_record(value_history):
    """Function to extrapolate the next value record based on the given value history."""

    diffs = [value_history]

    while not all((value_record == 0 for value_record in diffs[-1])):
        next_diff = []
        for i, j in zip(diffs[-1][:-1], diffs[-1][1:]):
            next_diff.append(j - i)
        diffs.append(next_diff)

    for prev, last in zip(diffs[:-1][::-1], diffs[1:][::-1]):
        prev.append(last[-1] + prev[-1])

    return diffs[0][-1]


if __name__ == "__main__":
    main()
