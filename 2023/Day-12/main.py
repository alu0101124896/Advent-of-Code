"""
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: September 2024
Description: This program implements my solution to the Advent of Code challenge.
"""

import re


def main():
    """Main function to resolve the challenge."""

    springs_condition_records = parse_data()

    total_posible_arrangements = 0
    for spring_condition_record in springs_condition_records[0]:
        total_posible_arrangements += count_posible_record_arrangements(
            spring_condition_record
        )

    print("The solution", total_posible_arrangements)


def parse_data():
    """Function to parse the input data of the challenge."""

    # input_file = input("\nInput file: ")
    input_file = "test.txt"

    with open(input_file, "r", encoding="utf-8") as infile:
        rawdata = infile.read().split("\n")

    if rawdata[-1] == "":
        rawdata.pop(-1)

    springs_condition_records = []
    for line in rawdata:
        damaged_record, control_values = line.split(" ")

        springs_condition_records.append(
            {
                "damaged_record": damaged_record,
                "record_size": len(damaged_record),
                "control_values": [int(value) for value in control_values.split(",")],
            }
        )

    return springs_condition_records


def count_posible_record_arrangements(spring_condition_record):
    """Function to # ToDo: Add function info."""

    regexp = ""
    damaged_positions = []
    for index, value in enumerate(spring_condition_record["damaged_record"]):
        if value == ".":
            regexp += r"\."

        elif value == "#":
            regexp += r"#"

        else:
            regexp += r"(\.|#)"
            damaged_positions.append(index)

    for arrangement in record_arrangements(
        spring_condition_record,
        record_size=spring_condition_record["record_size"],
    ):
        if re.match(regexp, arrangement):
            print(arrangement.split("."))

    return 0


def record_arrangements(spring_condition_record, record_size):
    if record_size == 0:
        return [""]

    current_condition_value = spring_condition_record["damaged_record"][-record_size]

    current_record_arrangements = record_arrangements(
        spring_condition_record,
        record_size - 1,
    )

    if current_condition_value == ".":
        return [
            "." + record_arrangement
            for record_arrangement in current_record_arrangements
        ]

    elif current_condition_value == "#":
        return [
            "#" + record_arrangement
            for record_arrangement in current_record_arrangements
        ]

    else:
        return [
            "." + record_arrangement
            for record_arrangement in current_record_arrangements
        ].extend(
            [
                "#" + record_arrangement
                for record_arrangement in current_record_arrangements
            ]
        )


if __name__ == "__main__":
    main()
