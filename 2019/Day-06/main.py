'''
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: October 2022
Description: This program implemets my solution to the Advent of Code challenge.
'''

from orbit_map import OrbitMap


def main():
    '''Main function to resolve the challenge.'''

    orbits = parse_data()

    print("\nPart one:")

    orbits_map = OrbitMap(orbits)

    print("  The total number of direct and indirect orbits is:",
          orbits_map.get_orbital_weight())

    print("\nPart two:")

    solution = orbits_map.get_path_to_santa()

    print("  The minimum number of orbital transfers is:", solution, end="\n\n")


def parse_data():
    '''Funcion to parse the input data of the challenge.'''

    input_file = input("\nInput file: ")

    with open(input_file, 'r', encoding="utf-8") as infile:
        rawdata = infile.read().split()

    orbits = [line.split(")") for line in rawdata]

    return orbits


if __name__ == "__main__":
    main()
