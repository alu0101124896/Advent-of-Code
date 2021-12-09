'''
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2021
Description: This program implemets my solution to the Advent of Code challenge.
'''

from functools import reduce


def main():
    '''Main function to resolve the challenge.'''
    heightmap = parse_data()

    low_points = find_low_points(heightmap)
    # risk_level = get_risk_level(low_points, heightmap)
    basins = find_largest_basins(low_points, heightmap)

    # print("\nThe sum of the risk levels of all low points is:", risk_level)
    print("\nThe multiplication of the sizes of the three largest basins is:",
          basins)


def parse_data():
    '''Funcion to parse the input data of the challenge.'''
    input_file = input("\nInput file: ")
    data = open(input_file, 'r').read().split("\n")

    if data[len(data) - 1] == '':
        data.pop()

    return [[int(number) for number in line] for line in data]


def find_low_points(heightmap):
    '''Function to obtain the low points on the heightmap.'''
    low_points = []
    for line_index, line in enumerate(heightmap):
        for point_index, point_value in enumerate(line):
            if line_index - 1 >= 0 \
               and heightmap[line_index - 1][point_index] <= point_value \
               or line_index + 1 <= len(heightmap) - 1 \
               and heightmap[line_index + 1][point_index] <= point_value \
               or point_index - 1 >= 0\
               and heightmap[line_index][point_index - 1] <= point_value \
               or point_index + 1 <= len(line) - 1 \
               and heightmap[line_index][point_index + 1] <= point_value:
                continue

            else:
                low_points.append((line_index, point_index))

    return low_points


def get_risk_level(low_points, heightmap):
    '''Function to obtain the sum of the risks of all low points.'''
    risk_level = 0
    for point in low_points:
        risk_level += heightmap[point[0]][point[1]] + 1
    return risk_level


def find_largest_basins(low_points, heightmap):
    '''Function to obtain the sizes of the three largest basins multiplied
    together.'''
    basin_sizes = []
    for low_point in low_points:
        basin = set()
        new_points = {low_point}

        while len(new_points) != 0:
            next_new_points = set()
            for point in new_points:
                for adjacen_point in get_in_basin_adjacents(point, heightmap):
                    if not basin.issuperset({adjacen_point}):
                        next_new_points.add(adjacen_point)

            basin.update(new_points)
            new_points = next_new_points.copy()
            next_new_points.clear()

        basin_sizes.append(len(basin))

    basin_sizes.sort()
    return reduce(lambda x, y: x * y, basin_sizes[-3:])


def get_in_basin_adjacents(point, heightmap):
    '''Function to obtain the adjacent points that are part of the same
    basin.'''
    lower_adjacents = set()
    if point[0] - 1 >= 0 and heightmap[point[0] - 1][point[1]] < 9:
        lower_adjacents.add((point[0] - 1, point[1]))

    if point[0] + 1 <= len(heightmap) - 1 \
            and heightmap[point[0] + 1][point[1]] < 9:
        lower_adjacents.add((point[0] + 1, point[1]))

    if point[1] - 1 >= 0 and heightmap[point[0]][point[1] - 1] < 9:
        lower_adjacents.add((point[0], point[1] - 1))

    if point[1] + 1 <= len(heightmap[0]) - 1 \
            and heightmap[point[0]][point[1] + 1] < 9:
        lower_adjacents.add((point[0], point[1] + 1))

    return lower_adjacents


if __name__ == "__main__":
    main()
