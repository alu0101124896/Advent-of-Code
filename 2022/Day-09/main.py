"""
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2022
Description: This program implements my solution to the Advent of Code
 challenge.
"""

from rope_knot import RopeKnot


def main():
    """Main function to resolve the challenge."""

    directions = parse_data()

    print("\nPart one:")

    head, tail = follow(directions)
    part_one_solution = len(tail.unique_positions())

    print("  The number of unique positions is:", part_one_solution)


def parse_data():
    """Function to parse the input data of the challenge."""

    input_file = input("\nInput file: ")

    with open(input_file, 'r', encoding="utf-8") as infile:
        raw_data = infile.read().split("\n")

    if raw_data[-1] == "":
        raw_data.pop()

    raw_directions = [line.split(" ") for line in raw_data]
    directions = [(line[0], int(line[1])) for line in raw_directions]

    return directions


def follow(directions):
    """Function to move a rope following the given directions."""

    head = RopeKnot()
    tail = RopeKnot()

    for direction, n_steps in directions:
        for _ in range(n_steps):
            head.move_towards(direction)
            if not tail.is_touching(head):
                tail.move_to(head.prev_location())

    return head, tail


if __name__ == "__main__":
    main()
