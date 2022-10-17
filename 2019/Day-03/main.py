'''
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: # ToDo: Add date
Description: This program implemets my solution to the Advent of Code challenge.
'''

import numpy as np
from scipy.spatial.distance import cityblock

CENTRAL_POINT = np.array([0, 0])


def main():
    '''Main function to resolve the challenge.'''

    wires_directions = parse_data()
    wires_paths = directions_to_paths(wires_directions)

    intersections = set(wires_paths[0]).intersection(set(wires_paths[1]))

    print("\nPart one:")

    closest_intersection = find_closest_intersection(intersections)

    print("  The distance to the closest intersection is:",
          closest_intersection)

    print("\nPart two:")

    fewest_steps_intersection = find_fewest_steps_intersection(
        intersections, wires_paths)

    print("  The fewest combined steps to an intersection is:",
          fewest_steps_intersection,
          end="\n\n")


def parse_data() -> list[list[tuple[str, int]]]:
    '''Funcion to parse the input data of the challenge.'''

    input_file = input("\nInput file: ")

    with open(input_file, 'r', encoding="utf-8") as infile:
        rawdata = infile.read().split()

    wires_directions = [[(direction[0], int(direction[1:]))
                         for direction in directions.split(',')]
                        for directions in rawdata]

    return wires_directions


def directions_to_paths(
    wires_directions: list[list[tuple[str,
                                      int]]]) -> list[list[tuple[str, int]]]:
    '''Function to get all positions of the grid where each wire goes through.
    '''

    wires_paths = []

    for directions in wires_directions:
        wire_path = []
        last_position = CENTRAL_POINT.copy()

        for direction in directions:
            if direction[0] == 'R':
                movement = (1, 0)
            elif direction[0] == 'L':
                movement = (-1, 0)
            elif direction[0] == 'U':
                movement = (0, 1)
            elif direction[0] == 'D':
                movement = (0, -1)

            for _ in range(direction[1]):
                last_position = last_position + movement
                wire_path.append(tuple(last_position))

        wires_paths.append(wire_path)

    return wires_paths


def find_closest_intersection(intersections: set[tuple[str, int]]) -> int:
    '''Function to find the Manhatan distance of the closest intersection of two
    wires from the central point.'''

    closest_intersection = min(
        cityblock(CENTRAL_POINT, intersection)
        for intersection in intersections)

    return closest_intersection


def find_fewest_steps_intersection(
        intersections: set[tuple[str, int]],
        wires_paths: list[list[tuple[str, int]]]) -> int:
    '''Function to find the fewest combined steps the wires must take to reach
    an intersection.'''

    intersections_steps = []

    for intersection in intersections:
        current_intersection_steps = 0

        for wire_path in wires_paths:
            current_intersection_steps += wire_path.index(intersection) + 1

        intersections_steps.append(current_intersection_steps)

    return min(intersections_steps)


if __name__ == "__main__":
    main()
