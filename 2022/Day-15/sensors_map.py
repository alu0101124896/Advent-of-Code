"""
File: sensors_map.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2022
Description: This program implements my solution to the Advent of Code
 challenge.
"""


def distance(point_1, point_2):
    """Function to calculate the Manhattan distance between the two given
    points."""

    return abs(point_2[0] - point_1[0]) + abs(point_2[1] - point_1[1])


class SensorsMap:
    """Class to represent a sensors map."""

    def __init__(self, sensors_reports):
        self.sensors_reports = sensors_reports

        self.grid = {}
        for sensor, beacon in self.sensors_reports:
            self.grid[sensor] = "S"
            self.grid[beacon] = "B"

    def count_empty_cells(self, row):
        """Function to count the number of positions in the given row where a
        beacon cannot be present."""

        empty_cells = set()

        for sensor, beacon in self.sensors_reports:
            current_distance = distance(sensor, beacon)

            for i in range(sensor[0] - current_distance,
                           sensor[0] + current_distance + 1):
                if (self.grid.get((i, row), ".") == "." and
                        distance((i, row), sensor) <= current_distance):
                    empty_cells.add(i)

        return empty_cells

    def find_distress_beacon(self, lower_bound, upper_bound):
        """Function to find the only position where a beacon can be
        undetected."""

        for sensor, beacon in self.sensors_reports:
            current_distance = distance(sensor, beacon) + 1

            for i in range(sensor[0] - current_distance,
                           sensor[0] + current_distance + 1):
                perimeter_idx = current_distance - abs(sensor[0] - i)
                for j in {sensor[1] - perimeter_idx,
                          sensor[1] + perimeter_idx}:

                    if (lower_bound < i < upper_bound and
                            lower_bound < j < upper_bound and
                            all(((distance(sensor, (i, j)) >
                                  distance(sensor, beacon))
                                 for sensor, beacon in self.sensors_reports))):
                        return i, j
