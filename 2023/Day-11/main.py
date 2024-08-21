"""
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: August 2024
Description: This program implements my solution to the Advent of Code challenge.
"""


def main():
    """Main function to resolve the challenge."""

    galaxy_locations, empty_rows, empty_cols = parse_data()

    spatial_distance = get_spatial_distance(galaxy_locations, empty_rows, empty_cols)

    print("The total distance between all galaxies is:", spatial_distance)


def parse_data():
    """Function to parse the input data of the challenge."""

    input_file = input("\nInput file: ")

    with open(input_file, "r", encoding="utf-8") as infile:
        rawdata = infile.read().split("\n")

    if rawdata[-1] == "":
        rawdata.pop(-1)

    galaxy_locations = [
        (i, j)
        for i, map_line in enumerate(rawdata)
        for j, map_tile in enumerate(map_line)
        if map_tile == "#"
    ]

    not_empty_rows, not_empty_cols = zip(*galaxy_locations)

    empty_rows = {row for row in range(len(rawdata)) if row not in not_empty_rows}
    empty_cols = {col for col in range(len(rawdata[0])) if col not in not_empty_cols}

    return galaxy_locations, empty_rows, empty_cols


def get_spatial_distance(galaxy_locations, empty_rows, empty_cols):
    """
    Function to calculate the sum of distances between each pair of the given galaxies.
    """

    spatial_distance = 0

    for i, a_galaxy_location in enumerate(galaxy_locations):
        for b_galaxy_location in galaxy_locations[i:]:
            current_pair_dist = 0

            current_pair_dist += abs(a_galaxy_location[0] - b_galaxy_location[0])
            current_pair_dist += abs(a_galaxy_location[1] - b_galaxy_location[1])

            for row in empty_rows:
                if (
                    a_galaxy_location[0] < row < b_galaxy_location[0]
                    or a_galaxy_location[0] > row > b_galaxy_location[0]
                ):
                    current_pair_dist += 1

            for col in empty_cols:
                if (
                    a_galaxy_location[1] < col < b_galaxy_location[1]
                    or a_galaxy_location[1] > col > b_galaxy_location[1]
                ):
                    current_pair_dist += 1

            spatial_distance += current_pair_dist

    return spatial_distance


if __name__ == "__main__":
    main()
