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

    print("\nPart two:")

    part_two_solution = get_best_scenic_score(trees_grid)

    print("  The best scenic score is:", part_two_solution)


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


def get_best_scenic_score(trees_grid):
    """Function to get the best tree's scenic score of the grid."""

    best_scenic_score = 0

    for row in range(1, len(trees_grid) - 1):
        for col in range(1, len(trees_grid[row]) - 1):

            current_tree_scenic_score = get_scenic_score(row, col, trees_grid)

            if best_scenic_score < current_tree_scenic_score:
                best_scenic_score = current_tree_scenic_score

    return best_scenic_score


def get_scenic_score(row, col, trees_grid):
    """Function to get the given tree's scenic score on the given grid."""

    # Look up
    up_scenic_score = 0
    for i in range(row - 1, -1, -1):
        up_scenic_score += 1

        if trees_grid[row][col] <= trees_grid[i][col]:
            break

    # Look down
    down_scenic_score = 0
    for i in range(row + 1, len(trees_grid)):
        down_scenic_score += 1

        if trees_grid[row][col] <= trees_grid[i][col]:
            break

    # Look left
    left_scenic_score = 0
    for i in range(col - 1, -1, -1):
        left_scenic_score += 1

        if trees_grid[row][col] <= trees_grid[row][i]:
            break

    # Look right
    right_scenic_score = 0
    for i in range(col + 1, len(trees_grid[row])):
        right_scenic_score += 1

        if trees_grid[row][col] <= trees_grid[row][i]:
            break

    return (
        up_scenic_score
        * down_scenic_score
        * left_scenic_score
        * right_scenic_score
    )


if __name__ == "__main__":
    main()
