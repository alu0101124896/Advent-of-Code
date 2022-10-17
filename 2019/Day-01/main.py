'''
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: October 2022
Description: This program implemets my solution to the Advent of Code challenge.
'''

from math import floor


def main():
    '''Main function to resolve the challenge.'''

    modules_mass = parse_data()

    print("\nPart one:")

    module_fuel = sum(
        required_fuel(module_mass, False) for module_mass in modules_mass)

    print("  The fuel required only for the module mass is:", module_fuel)

    print("\nPart two:")

    total_fuel = sum(
        required_fuel(module_mass, True) for module_mass in modules_mass)

    print("  The total fuel required is:", total_fuel, end="\n\n")


def parse_data():
    '''Funcion to parse the input data of the challenge.'''

    input_file = input("\nInput file: ")

    with open(input_file, 'r', encoding="utf-8") as infile:
        rawdata = infile.read().split()

    modules_mass = [int(module_mass) for module_mass in rawdata]

    return modules_mass


def required_fuel(mass: int, recursive: bool) -> int:
    '''Function to find the fuel required to launch a given module based on its
    mass.'''

    fuel_for_module = floor(mass / 3) - 2

    if not recursive:
        return fuel_for_module

    fuel_for_fuel = required_recursive_fuel(fuel_for_module)

    return fuel_for_module + fuel_for_fuel


def required_recursive_fuel(prev_fuel: int) -> int:
    '''Function to find the fuel required to launch a given module based on its
    mass and the mass of the required fuel.'''

    new_fuel = floor(prev_fuel / 3) - 2

    if new_fuel <= 0:
        return 0

    return new_fuel + required_recursive_fuel(new_fuel)


if __name__ == "__main__":
    main()
