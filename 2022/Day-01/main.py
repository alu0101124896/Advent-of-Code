"""
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2022
Description: This program implements my solution to the Advent of Code
 challenge.
"""


def main():
    """Main function to resolve the challenge."""

    elves_food = parse_data()

    solution = get_most_carried_calories(elves_food)

    print("\nThe number of calories carried by the elf carrying the most is:",
          solution)


def parse_data():
    """Function to parse the input data of the challenge."""

    input_file = input("\nInput file: ")

    with open(input_file, 'r', encoding="utf-8") as infile:
        raw_data = infile.read().split("\n\n")

    elves_food = [[int(calories) for calories in elf_food.split()]
                  for elf_food in raw_data]

    return elves_food


def get_most_carried_calories(elves_food):

    elves_calories = [sum(elf_food) for elf_food in elves_food]

    return max(elves_calories)


if __name__ == "__main__":
    main()
