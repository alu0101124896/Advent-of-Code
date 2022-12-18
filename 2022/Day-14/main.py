"""
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2022
Description: This program implements my solution to the Advent of Code
 challenge.
"""

from itertools import pairwise


def main():
    """Main function to resolve the challenge."""

    rock_paths = parse_data()
    sand_entry_point = (500, 0)
    cave_system = generate_cave_system(rock_paths)

    print("\nPart one:")

    part_one_solution, _ = simulate_sand_fall(sand_entry_point, cave_system)

    print("  The number of resting units of sand is:", part_one_solution)


def parse_data():
    """Function to parse the input data of the challenge."""

    input_file = input("\nInput file: ")

    with open(input_file, 'r', encoding="utf-8") as infile:
        raw_data = infile.read().split("\n")

    if raw_data[-1] == "":
        raw_data.pop()

    rock_paths = [[[int(coord) for coord in location.split(",")]
                   for location in rock_path.split(" -> ")]
                  for rock_path in raw_data]

    return rock_paths


def generate_cave_system(rock_paths):
    """Function to generate the internal layout of the cave system from the
    given rock paths."""

    cave_system = [
        ["."
         for _ in range(
            max((y_coord
                 for rock_path in rock_paths
                 for _, y_coord in rock_path)) + 1)
         ]
        for _ in range(
            max((x_coord
                 for rock_path in rock_paths
                 for x_coord, _ in rock_path)) + 1)
    ]

    for rock_path in rock_paths:
        for point_one, point_two in pairwise(rock_path):
            cave_system = set_wall(point_one, point_two, cave_system)

    return cave_system


def set_wall(point_one, point_two, cave_system):
    """Function to set a wall between the two given points inside the given
    cave system."""

    begin_idx, end_idx = (
        (point_one[0], point_two[0])
        if point_one[0] <= point_two[0]
        else (point_two[0], point_one[0])
    )
    begin_jdx, end_jdx = (
        (point_one[1], point_two[1])
        if point_one[1] <= point_two[1]
        else (point_two[1], point_one[1])
    )

    for i in range(begin_idx, end_idx + 1):
        for j in range(begin_jdx, end_jdx + 1):
            cave_system[i][j] = "#"

    return cave_system


def simulate_sand_fall(sand_entry_point, cave_system):
    """Function to simulate a sand fall from the given entry point into the
     given cave system"""

    resting_sand_units = 0

    while True:
        sand_pos = list(sand_entry_point)
        try:
            while True:
                # Down
                if cave_system[sand_pos[0]][sand_pos[1] + 1] == ".":
                    cave_system[sand_pos[0]][sand_pos[1] + 1] = "o"
                    cave_system[sand_pos[0]][sand_pos[1]] = "."
                    sand_pos[1] += 1

                # Down-left
                elif cave_system[sand_pos[0] - 1][sand_pos[1] + 1] == ".":
                    cave_system[sand_pos[0] - 1][sand_pos[1] + 1] = "o"
                    cave_system[sand_pos[0]][sand_pos[1]] = "."
                    sand_pos[0] -= 1
                    sand_pos[1] += 1

                # Down-right
                elif cave_system[sand_pos[0] + 1][sand_pos[1] + 1] == ".":
                    cave_system[sand_pos[0] + 1][sand_pos[1] + 1] = "o"
                    cave_system[sand_pos[0]][sand_pos[1]] = "."
                    sand_pos[0] += 1
                    sand_pos[1] += 1

                # Resting position found
                else:
                    resting_sand_units += 1
                    break

        except IndexError:
            cave_system[sand_pos[0]][sand_pos[1]] = "."
            break

    return resting_sand_units, cave_system


if __name__ == "__main__":
    main()
