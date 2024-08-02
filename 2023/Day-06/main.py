"""
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: August 2024
Description: This program implements my solution to the Advent of Code challenge.
"""


def main():
    """Main function to resolve the challenge."""

    leaderboard = parse_data()

    winning_error_margin = 1
    for race_info in leaderboard:
        winning_error_margin *= record_breaking_ways(race_info)

    print("The winning error margin is", winning_error_margin)


def parse_data():
    """Function to parse the input data of the challenge."""

    input_file = input("\nInput file: ")

    with open(input_file, "r", encoding="utf-8") as infile:
        rawdata = infile.read().split("\n")

    time_data = [int(time_entry) for time_entry in rawdata[0].split()[1:]]
    record_distance_data = [
        int(record_distance_entry) for record_distance_entry in rawdata[1].split()[1:]
    ]

    leaderboard = list(zip(time_data, record_distance_data))

    return leaderboard


def record_breaking_ways(race_info):
    """Function to calculate the number of ways to break the record of a given boat race."""

    race_time, race_record = race_info

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
