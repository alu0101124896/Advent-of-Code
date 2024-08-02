"""
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: August 2024
Description: This program implements my solution to the Advent of Code challenge.
"""


def main():
    """Main function to resolve the challenge."""

    time_data, record_distance_data = parse_data()

    # Part 1

    winning_error_margin = 1
    for race_time, race_record in zip(time_data, record_distance_data):
        winning_error_margin *= record_breaking_ways(int(race_time), int(race_record))

    print("The expected winning error margin is", winning_error_margin)

    # Part 2

    real_time_data = "".join(time_data)
    real_record_distance_data = "".join(record_distance_data)

    real_winning_error_margin = record_breaking_ways(
        int(real_time_data), int(real_record_distance_data)
    )

    print("The real winning error margin is", real_winning_error_margin)


def parse_data():
    """Function to parse the input data of the challenge."""

    input_file = input("\nInput file: ")

    with open(input_file, "r", encoding="utf-8") as infile:
        rawdata = infile.read().split("\n")

    time_data = rawdata[0].split()[1:]
    record_distance_data = rawdata[1].split()[1:]

    return time_data, record_distance_data


def record_breaking_ways(race_time, race_record):
    """Function to calculate the number of ways to break the record of a given boat race."""

    num_record_breaking_ways = sum(
        (
            2
            if (boat_charging_time * (race_time - boat_charging_time)) > race_record
            else 0
        )
        for boat_charging_time in range(1, race_time // 2)
    )

    if (race_time % 2) == 0:
        num_record_breaking_ways += 1
    else:
        num_record_breaking_ways += 2

    return num_record_breaking_ways


if __name__ == "__main__":
    main()
