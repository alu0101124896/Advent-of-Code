"""
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2022
Description: This program implements my solution to the Advent of Code
 challenge.
"""

from cell import Cell


def main():
    """Main function to resolve the challenge."""

    start, end, grid = parse_data()

    print("\nPart one:")

    part_one_solution = len(get_shortest_path(start, end, grid))

    print("  The shortest path's length is:", part_one_solution)


def parse_data():
    """Function to parse the input data of the challenge."""

    input_file = input("\nInput file: ")

    with open(input_file, 'r', encoding="utf-8") as infile:
        raw_data = infile.read().split("\n")

    if raw_data[-1] == "":
        raw_data.pop()

    start = get_position("S", raw_data)
    end = get_position("E", raw_data)

    grid = [[Cell(position=(i, j), height=char)
             for j, char in enumerate(line)]
            for i, line in enumerate(raw_data)]

    return start, end, grid


def get_position(value, grid):
    """Function to get the position a given value in a grid."""

    for i, row in enumerate(grid):
        try:
            j = row.index(value)
        except ValueError:
            pass
        else:
            return i, j

    return None


def get_shortest_path(start_location, end_location, grid):
    """Function to get the shortest path on the given heightmap."""

    unvisited_locations = []
    for line in grid:
        for cell in line:
            unvisited_locations.append(cell)

    grid[start_location[0]][start_location[1]].distance = 0

    while len(unvisited_locations) > 0:
        current_cell = min(unvisited_locations,
                           key=lambda location: location.distance)
        unvisited_locations.pop(unvisited_locations.index(current_cell))

        if current_cell.location() == end_location:
            break

        for neighbor in current_cell.get_neighbors(grid):
            if neighbor not in unvisited_locations:
                continue

            new_neighbor_distance = current_cell.distance + 1
            if neighbor.distance > new_neighbor_distance:
                neighbor.distance = new_neighbor_distance
                neighbor.previous_cell = current_cell

    path = []
    current_cell = grid[end_location[0]][end_location[1]]

    while (current_cell := current_cell.previous_cell) is not None:
        path.insert(0, current_cell.height)

    return path


if __name__ == "__main__":
    main()
