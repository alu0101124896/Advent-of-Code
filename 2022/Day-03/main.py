"""
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2022
Description: This program implements my solution to the Advent of Code
 challenge.
"""

PRIORITY_ORDER = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main():
    """Main function to resolve the challenge."""

    rucksacks = parse_data()

    print("\nPart one:")

    shared_items = get_shared_items(rucksacks)
    part_one_solution = sum(get_priority_values(shared_items))

    print("  The total sum of the priority values is:", part_one_solution)


def parse_data():
    """Function to parse the input data of the challenge."""

    input_file = input("\nInput file: ")

    with open(input_file, 'r', encoding="utf-8") as infile:
        raw_data = infile.read().split("\n")

    if raw_data[-1] == "":
        raw_data.pop()

    return raw_data


def get_shared_items(rucksacks):
    """Function to get the item type that appears in both compartments of each
    rucksack."""

    shared_items = []

    for rucksack in rucksacks:
        first_compartment = {*rucksack[:len(rucksack) // 2]}
        second_compartment = {*rucksack[len(rucksack) // 2:]}

        shared_items.append(
            *first_compartment.intersection(second_compartment)
        )

    return shared_items


def get_priority_values(items):
    """Function to get the priority values of the given list of items."""

    return (PRIORITY_ORDER.index(item) + 1 for item in items)


if __name__ == "__main__":
    main()
