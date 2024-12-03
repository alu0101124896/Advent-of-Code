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

    possible_approaches = get_possible_approaches(valves_report)

    print("\nPart one:")

    part_one_solution = get_most_pressure_release_1p(possible_approaches)

    print("  The most pressure you can release alone is:", part_one_solution)

    # print("\nPart two:")
    #
    # part_two_solution = get_most_pressure_release_2p(possible_approaches)
    #
    # print("  The most pressure you can release with one elephant's help is:",
    #       part_two_solution)


def parse_data():
    """Function to parse the input data of the challenge."""

    # input_file = input("\nInput file: ")
    input_file = "test.txt"

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


def get_possible_approaches(
        valves_report,
        minutes_left=30,
        current_path=["AA"],
        open_valves=[],
        released_pressure=0,
):
    """Function to get the most possible pressure you can release in the given
     scenario."""

    if minutes_left <= 0:
        return [current_path]

    possible_approaches = []
    possible_paths = [
        possible_path
        for possible_path in get_possible_steps(
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
        return [current_path]

    for possible_path in possible_paths:
        possible_approaches.extend(
            get_possible_approaches(
                valves_report,
                minutes_left - len(possible_path),
                current_path + possible_path[1:],
                open_valves + [possible_path[-1]],
                released_pressure + (
                        current_pressure_per_minute * len(possible_path)
                ),
            )
        )

    return possible_approaches


def get_possible_steps(
        valves_report,
        minutes_left,
        current_steps,
        open_valves,
):
    """Function to get all possible paths to the closed valves with some
    positive flow rate."""

    possible_steps = []

    if len(current_steps) > minutes_left:
        return possible_steps

    if (valves_report[current_steps[-1]]["flow_rate"] != 0
            and current_steps[-1] not in open_valves):
        possible_steps.append(current_steps)

    for adjacent_valve in valves_report[current_steps[-1]]["adjacent_valves"]:
        if adjacent_valve not in current_steps:
            possible_steps.extend(
                get_possible_steps(
                    valves_report,
                    minutes_left,
                    current_steps + [adjacent_valve],
                    open_valves,
                )
            )

    return possible_steps


def get_most_pressure_release_1p(possible_approaches):
    """Fff"""

    pressure_releases =

    for possible_approach in possible_approaches:

    return max()



# def get_most_pressure_release_2p(possible_approaches):
#     """Fff"""
#
#     pass



if __name__ == "__main__":
    main()
