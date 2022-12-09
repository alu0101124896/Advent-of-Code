"""
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2022
Description: This program implements my solution to the Advent of Code
 challenge.
"""

from directory_tree import DirectoryTree


def main():
    """Main function to resolve the challenge."""

    terminal_output = parse_data()

    print("\nPart one:")

    filesystem = DirectoryTree(terminal_output)
    part_one_solution = sum(get_directory_sizes(filesystem, max_size=100000))

    print("  The total size is:", part_one_solution)

    print("\nPart two:")

    (directory_to_delete,
     part_two_solution) = get_directory_to_delete(filesystem)

    print("  The total size is:", part_two_solution)


def parse_data():
    """Function to parse the input data of the challenge."""

    input_file = input("\nInput file: ")

    with open(input_file, 'r', encoding="utf-8") as infile:
        raw_data = infile.read().split("\n")

    if raw_data[-1] == "":
        raw_data.pop()

    terminal_output = [line.split(" ") for line in raw_data]

    return terminal_output


def get_directory_sizes(filesystem, max_size=None):
    """Function to get the sizes of the directories of the given filesystem."""

    directory_sizes = []

    for directory in filesystem.get_all_directories():
        current_directory_size = directory.get_total_size()

        if max_size is None or current_directory_size <= max_size:
            directory_sizes.append(current_directory_size)

    return directory_sizes


def get_directory_to_delete(filesystem):
    """Function to get the smallest directory to free enough space to update
    the system."""

    total_available_space = 70000000
    needed_free_space = 30000000
    current_free_space = total_available_space - filesystem.get_total_size()

    candidate_directories = []
    for current_directory in filesystem.get_all_directories():
        current_directory_size = current_directory.get_total_size()

        if (current_free_space + current_directory_size) > needed_free_space:
            candidate_directories.append((current_directory,
                                         current_directory_size))

    return min(candidate_directories, key=lambda candidate: candidate[1])


if __name__ == "__main__":
    main()
