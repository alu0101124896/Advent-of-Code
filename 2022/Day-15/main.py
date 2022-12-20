"""
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2022
Description: This program implements my solution to the Advent of Code
 challenge.
"""

import re

from sensors_map import SensorsMap


def main():
    """Main function to resolve the challenge."""

    sensors_reports = parse_data()
    sensors_map = SensorsMap(sensors_reports)

    print("\nPart one:")

    row_to_look_at = int(input("  Row to look at: "))
    part_one_solution = len(sensors_map.count_empty_cells(row_to_look_at))

    print("  The number positions where a beacon cannot be present is:",
          part_one_solution)

    print("\nPart two:")

    lower_bound = int(input("  Lower bound: "))
    upper_bound = int(input("  Upper bound: "))

    distress_beacon = sensors_map.find_distress_beacon(lower_bound,
                                                       upper_bound)

    part_two_solution = (distress_beacon[0] * 4000000) + distress_beacon[1]

    print("  The tuning frequency of the distress beacon's position is:",
          part_two_solution)


def parse_data():
    """Function to parse the input data of the challenge."""

    input_file = input("\nInput file: ")

    with open(input_file, 'r', encoding="utf-8") as infile:
        raw_data = infile.read().split("\n")

    if raw_data[-1] == "":
        raw_data.pop()

    reg_exp = re.compile(r"""
        .*
        x=(?P<sensor_x>-*\d+),\ y=(?P<sensor_y>-*\d+)
        .*
        x=(?P<beacon_x>-*\d+),\ y=(?P<beacon_y>-*\d+)
        .*
    """, re.VERBOSE)

    sensors_reports = []
    for line in raw_data:
        coords = re.match(reg_exp, line)
        sensor = int(coords.group("sensor_x")), int(coords.group("sensor_y"))
        beacon = int(coords.group("beacon_x")), int(coords.group("beacon_y"))

        sensors_reports.append((sensor, beacon))

    return sensors_reports


if __name__ == "__main__":
    main()
