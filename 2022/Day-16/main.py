"""
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2022
Description: This program implements my solution to the Advent of Code
 challenge.
"""

import re


def main():
    """Main function to resolve the challenge."""

    valves_report = parse_data()

    print("\nPart one:")

    part_one_solution = get_most_pressure_release(
        valves_report,
        minutes_left=30,
        current_path=["AA"],
        open_valves=[],
        released_pressure=0,
    )

    print("  The most pressure you can release is:", part_one_solution)


def parse_data():
    """Function to parse the input data of the challenge."""

    input_file = input("\nInput file: ")

    with open(input_file, 'r', encoding="utf-8") as infile:
        raw_data = infile.read().split("\n")

    if raw_data[-1] == "":
        raw_data.pop()

    reg_exp = re.compile(r"""
        .*
        Valve\ (?P<current_valve>[A-Z]+)
        .*
        rate=(?P<flow_rate>\d+)
        .*
        valve(s)*\ (?P<adjacent_valves>[A-Z]+(,\ [A-Z]+)*)
        .*
    """, re.VERBOSE)

    valves_report = {}
    for line in raw_data:
        coords = re.match(reg_exp, line)

        valves_report[coords.group("current_valve")] = {
            "flow_rate": int(coords.group("flow_rate")),
            "adjacent_valves": set(
                coords.group("adjacent_valves").split(", ")
            ),
        }

    return valves_report


def get_most_pressure_release(
        valves_report,
        minutes_left,
        current_path,
        open_valves,
        released_pressure,
):
    """Function to get the most possible pressure you can release in the given
     scenario."""

    if minutes_left <= 0:
        return released_pressure

    possible_pressure_releases = []
    possible_paths = [
        possible_path
        for possible_path in get_possible_paths(
            valves_report,
            minutes_left,
            [current_path[-1]],
            open_valves,
        )
        if len(possible_path) < minutes_left
    ]

    current_pressure_per_minute = sum((
        valves_report[open_valve]["flow_rate"]
        for open_valve in open_valves
    ))

    if len(possible_paths) == 0:
        return released_pressure + (
                current_pressure_per_minute * minutes_left
        )

    for possible_path in possible_paths:
        possible_pressure_releases.append(
            get_most_pressure_release(
                valves_report,
                minutes_left - len(possible_path),
                current_path + possible_path[1:],
                open_valves + [possible_path[-1]],
                released_pressure + (
                        current_pressure_per_minute * len(possible_path)
                ),
            )
        )

    return max(possible_pressure_releases)


def get_possible_paths(
        valves_report,
        minutes_left,
        current_path,
        open_valves,
):
    """Function to get all possible paths to the closed valves with some
    positive flow rate."""

    possible_paths = []

    if len(current_path) > minutes_left:
        return possible_paths

    if (valves_report[current_path[-1]]["flow_rate"] != 0
            and current_path[-1] not in open_valves):
        possible_paths.append(current_path)

    for adjacent_valve in valves_report[current_path[-1]]["adjacent_valves"]:
        if adjacent_valve not in current_path:
            possible_paths.extend(
                get_possible_paths(
                    valves_report,
                    minutes_left,
                    current_path + [adjacent_valve],
                    open_valves,
                )
            )

    return possible_paths


if __name__ == "__main__":
    main()
