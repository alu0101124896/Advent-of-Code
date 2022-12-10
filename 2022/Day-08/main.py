"""
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2022
Description: This program implements my solution to the Advent of Code
 challenge.
"""


def main():
    """Main function to resolve the challenge."""

    trees_grid = parse_data()

    print("\nPart one:")

    part_one_solution = count_visible_trees(trees_grid)

    print("  The number of visible trees is:", part_one_solution)


def parse_data():
    """Function to parse the input data of the challenge."""

    input_file = input("\nInput file: ")

    with open(input_file, 'r', encoding="utf-8") as infile:
        raw_data = infile.read().split("\n")

    if raw_data[-1] == "":
        raw_data.pop()

    trees_grid = [[int(tree) for tree in line] for line in raw_data]

    return trees_grid


def count_visible_trees(trees_grid):
    """Function to count all visible trees from outside the given grid."""

    # Perimeter trees:
    total_count = (len(trees_grid) * 2) + ((len(trees_grid[0]) - 2) * 2)

    # Interior trees:
    for row in range(1, len(trees_grid) - 1):
        for col in range(1, len(trees_grid[row]) - 1):
            total_count += 1 if is_visible(row, col, trees_grid) else 0

    return total_count


def is_visible(row, col, grid):
    """Function to check if the tree on the given place is visible from outside
    the given grid."""

    return (
        # Look up
        all((grid[row][col] > line[col] for line in grid[:row]))

        # Look down
        or all((grid[row][col] > line[col] for line in grid[row + 1:]))

        # Look right
        or all((grid[row][col] > tree for tree in grid[row][:col]))

        # Look left
        or all((grid[row][col] > tree for tree in grid[row][col + 1:]))
    )


if __name__ == "__main__":
    main()
