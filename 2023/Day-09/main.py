"""
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: August 2024
Description: This program implements my solution to the Advent of Code challenge.
"""


def main():
    """Main function to resolve the challenge."""

    sensor_report = parse_data()

    # Part one

    extrapolated_next_values = [
        extrapolate_next_value_record(value_history) for value_history in sensor_report
    ]

    print("The sum of all extrapolated next values is", sum(extrapolated_next_values))

    # Part two

    extrapolated_prev_values = [
        extrapolate_next_value_record(value_history[::-1])
        for value_history in sensor_report
    ]

    print(
        "The sum of all extrapolated previous values is", sum(extrapolated_prev_values)
    )


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

    history_diffs = [value_history]

    while not all((value_record == 0 for value_record in history_diffs[-1])):
        next_history_diff = []

        for i, j in zip(history_diffs[-1][:-1], history_diffs[-1][1:]):
            next_history_diff.append(j - i)

        history_diffs.append(next_history_diff)

    for prev, last in zip(history_diffs[:-1][::-1], history_diffs[1:][::-1]):
        prev.append(last[-1] + prev[-1])

    return history_diffs[0][-1]


if __name__ == "__main__":
    main()
