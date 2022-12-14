"""
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2022
Description: This program implements my solution to the Advent of Code
 challenge.
"""

from copy import deepcopy

from cell import Cell


def main():
    """Main function to resolve the challenge."""

    start, end, grid = parse_data()

    print("\nPart one:")

    part_one_solution = len(get_shortest_path(grid, (start,), end))

    print("  The shortest path's length is:", part_one_solution)

    print("\nPart two:")

    part_two_starting_points = [
        cell.location()
        for line in grid
        for cell in line
        if cell.height == 1
    ]
    part_two_starting_points.append(start)

    part_two_solution = len(get_shortest_path(grid,
                                              part_two_starting_points,
                                              end))

    print("  The shortest path's length is:", part_two_solution)


def parse_data():
    """Function to parse the input data of the challenge."""

    input_file = input("\nInput file: ")

    with open(input_file, 'r', encoding="utf-8") as infile:
        raw_data = infile.read().split("\n")

    if raw_data[-1] == "":
        raw_data.pop()

    start = get_location("S", raw_data)
    end = get_location("E", raw_data)

    grid = [[Cell(location=(i, j), height=char)
             for j, char in enumerate(line)]
            for i, line in enumerate(raw_data)]

    return start, end, grid


def get_location(value, grid):
    """Function to get the position a given value in a grid."""

    for i, row in enumerate(grid):
        try:
            j = row.index(value)
        except ValueError:
            pass
        else:
            return i, j


def get_shortest_path(grid_initial_state, start_locations, end_location):
    """Function to get the shortest path on the given heightmap."""

    grid = deepcopy(grid_initial_state)
    unvisited_locations = []

    for line in grid:
        for cell in line:
            unvisited_locations.append(cell)

    grid[end_location[0]][end_location[1]].distance = 0

    while len(unvisited_locations) > 0:
        current_cell = min(unvisited_locations,
                           key=lambda location: location.distance)
        unvisited_locations.pop(unvisited_locations.index(current_cell))

        for neighbor in current_cell.get_neighbors(grid):
            if neighbor not in unvisited_locations:
                continue

            new_neighbor_distance = current_cell.distance + 1
            if neighbor.distance > new_neighbor_distance:
                neighbor.distance = new_neighbor_distance
                neighbor.next_cell = current_cell

    return min(get_all_paths(grid, start_locations),
               key=lambda path: len(path))


def get_all_paths(grid, start_locations):
    """Function to get all paths from each starting location."""

    paths = []
    for start_location in start_locations:

        current_path = []
        current_cell = grid[start_location[0]][start_location[1]]

        while (current_cell := current_cell.next_cell) is not None:
            current_path.append(current_cell)

        if len(current_path) > 0:
            paths.append(current_path)

    return paths


if __name__ == "__main__":
    main()
