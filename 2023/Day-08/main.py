"""
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: August 2024
Description: This program implements my solution to the Advent of Code challenge.
"""


def main():
    """Main function to resolve the challenge."""

    instructions, nodes_info = parse_data()

    num_steps = traverse_map(instructions, nodes_info, start="AAA", end="ZZZ")

    print("The number of steps required to reach 'ZZZ' is", num_steps)


def parse_data() -> tuple[str, dict[str, dict[str, str]]]:
    """Function to parse the input data of the challenge."""

    input_file = input("\nInput file: ")

    with open(input_file, "r", encoding="utf-8") as infile:
        rawdata = infile.read().split("\n\n")

    instructions = rawdata[0]

    nodes_info = {}
    for node_raw_info in rawdata[1].split("\n"):
        if node_raw_info == "":
            continue

        node_name, node_destinations = node_raw_info.split(" = ")
        left_destination, right_destination = node_destinations[1:-1].split(", ")

        nodes_info.update(
            {
                node_name: {
                    "L": left_destination,
                    "R": right_destination,
                }
            }
        )

    return instructions, nodes_info


def traverse_map(
    instructions: str,
    nodes_info: dict[str, dict[str, str]],
    start: str = "AAA",
    end: str = "ZZZ",
) -> int:
    """
    Function to calculate the number of steps needed to traverse a map between the given
     starting and ending points.
    """

    num_steps = 0
    current_location = start

    while current_location != end:

        current_step_direction = instructions[num_steps % len(instructions)]
        current_location = nodes_info[current_location][current_step_direction]

        num_steps += 1

    return num_steps


if __name__ == "__main__":
    main()
