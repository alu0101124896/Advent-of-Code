'''
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2021
Description: This program implemets my solution to the Advent of Code challenge.
'''

from math import floor


def main():
    '''Main function to resolve the challenge.'''

    modules_mass = parse_data()

    total_fuel = sum(required_fuel(module_mass) for module_mass in modules_mass)

    print("\nThe total fuel needed is:", total_fuel, end="\n\n")


def parse_data():
    '''Funcion to parse the input data of the challenge.'''

    input_file = input("\nInput file: ")

    with open(input_file, 'r', encoding="utf-8") as infile:
        rawdata = infile.read().split()

    modules_mass = [int(module_mass) for module_mass in rawdata]

    return modules_mass


def required_fuel(mass: int) -> int:
    '''Function to find the fuel required to launch a given module based on its
    mass.'''

    return floor(mass / 3) - 2


if __name__ == "__main__":
    main()
