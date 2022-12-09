"""
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2022
Description: This program implements my solution to the Advent of Code
 challenge.
"""

GAME_RULES_PART_ONE = {
    "A": {  # Rock
        "X": 1 + 3,  # Rock -> Draw
        "Y": 2 + 6,  # Paper -> Win
        "Z": 3 + 0,  # Scissors -> Loss
    },
    "B": {  # Paper
        "X": 1 + 0,  # Rock -> Loss
        "Y": 2 + 3,  # Paper -> Draw
        "Z": 3 + 6,  # Scissors -> Win
    },
    "C": {  # Scissors
        "X": 1 + 6,  # Rock -> Win
        "Y": 2 + 0,  # Paper -> Loss
        "Z": 3 + 3,  # Scissors -> Draw
    },
}

GAME_RULES_PART_TWO = {
    "A": {  # Rock
        "X": 0 + 3,  # Loss -> Scissors
        "Y": 3 + 1,  # Draw -> Rock
        "Z": 6 + 2,  # Win -> Paper
    },
    "B": {  # Paper
        "X": 0 + 1,  # Loss -> Rock
        "Y": 3 + 2,  # Draw -> Paper
        "Z": 6 + 3,  # Win -> Scissors
    },
    "C": {  # Scissors
        "X": 0 + 2,  # Loss -> Paper
        "Y": 3 + 3,  # Draw -> Scissors
        "Z": 6 + 1,  # Win -> Rock
    },
}


def main():
    """Main function to resolve the challenge."""

    strategy_guide = parse_data()

    print("\nPart one:")

    solution = get_total_score(strategy_guide, GAME_RULES_PART_ONE)

    print("  The total score is:", solution)

    print("\nPart two:")

    solution = get_total_score(strategy_guide, GAME_RULES_PART_TWO)

    print("  The total score is:", solution)


def parse_data():
    """Function to parse the input data of the challenge."""

    input_file = input("\nInput file: ")

    with open(input_file, 'r', encoding="utf-8") as infile:
        raw_data = infile.read().split("\n")

    if raw_data[-1] == "":
        raw_data.pop()

    strategy_guide = [game_round.split(" ") for game_round in raw_data]

    return strategy_guide


def get_total_score(strategy_guide, game_rules):
    """Function to get the total score of the game if everything goes exactly
    according to the given strategy guide."""

    total_score = 0

    for game_round in strategy_guide:
        prediction, response = game_round
        total_score += game_rules[prediction][response]

    return total_score


if __name__ == "__main__":
    main()
