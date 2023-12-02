"""
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2023
Description: This program implements my solution to the Advent of Code challenge.
"""


def main():
    """Main function to resolve the challenge."""

    previous_games_record = parse_data()

    # Part 1

    possible_games = get_possible_games(
        previous_games_record,
        bag_content={
            "red": 12,
            "green": 13,
            "blue": 14,
        }
    )

    print("The sum of the IDs of the possible games is:", sum(possible_games))

    # Part 2

    min_bag_content_per_game = [
        get_min_bag_content(game_record)
        for game_record in previous_games_record.values()
    ]

    powers_of_min_contents = [
        min_bag_content["red"] * min_bag_content["green"] * min_bag_content["blue"]
        for min_bag_content in min_bag_content_per_game
    ]

    print(
        "The sum of the powers of the minimum contents of each game is:",
        sum(powers_of_min_contents),
    )


def parse_data():
    """Function to parse the input data of the challenge."""

    input_file = input("\nInput file: ")

    with open(input_file, 'r', encoding="utf-8") as infile:
        rawdata = infile.read().split("\n")

    if rawdata[-1] == "":
        rawdata = rawdata[:-1]

    previous_games_record = {
        int(game.split(": ")[0].split(" ")[1]): [
            {
                color_group.split(" ")[1]: int(color_group.split(" ")[0])
                for color_group in batch.split(", ")
            }
            for batch in game.split(": ")[1].split("; ")
        ]
        for game in rawdata
    }

    return previous_games_record


def get_possible_games(previous_games_record, bag_content):
    """Function to get the games from the record that would have been possible if the
    bag had been loaded with the given content."""

    possible_games = []

    for game_id, game_record in previous_games_record.items():
        current_game_is_possible = True

        for batch in game_record:
            for color, cubes_count in batch.items():
                if cubes_count > bag_content[color]:
                    current_game_is_possible = False
                    break

            if not current_game_is_possible:
                break

        if current_game_is_possible:
            possible_games.append(game_id)

    return possible_games


def get_min_bag_content(game_record):
    """Function to get the minimum content inside the bag to be able to play a game
    resulting in the given record."""

    min_bag_content = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }

    for batch in game_record:
        for color, cubes_count in batch.items():
            if cubes_count > min_bag_content[color]:
                min_bag_content[color] = cubes_count

    return min_bag_content


if __name__ == "__main__":
    main()
