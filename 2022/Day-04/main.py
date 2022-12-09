"""
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2022
Description: This program implements my solution to the Advent of Code
 challenge.
"""


def main():
    """Main function to resolve the challenge."""

    elf_ranges = parse_data()

    print("\nPart one:")

    part_one_solution = len(get_fully_overlapped_ranges(elf_ranges))

    print("  The number of fully overlapped ranges is:", part_one_solution)


def parse_data():
    """Function to parse the input data of the challenge."""

    input_file = input("\nInput file: ")

    with open(input_file, 'r', encoding="utf-8") as infile:
        raw_data = infile.read().split("\n")

    if raw_data[-1] == "":
        raw_data.pop()

    elves_ranges = []
    for line in raw_data:

        elves_pair = []
        for elf_range in line.split(","):

            lower_bound, upper_bound = elf_range.split("-")
            elves_pair.append({*range(int(lower_bound), int(upper_bound) + 1)})

        elves_ranges.append(elves_pair)

    return elves_ranges


def get_fully_overlapped_ranges(elf_ranges):
    """Function to get all elf pairs in which one elf's range is fully
    contained on its pair elf's range."""

    overlapped_ranges = []
    for first_elf_range, second_elf_range in elf_ranges:

        if (first_elf_range.issubset(second_elf_range) or
                second_elf_range.issubset(first_elf_range)):
            overlapped_ranges.append((first_elf_range, second_elf_range))

    return overlapped_ranges


if __name__ == "__main__":
    main()
