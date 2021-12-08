'''
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2021
Description: This program implemets my solution to the Advent of Code challenge.
'''

import math


def main():
    '''Main function to resolve the challenge.'''
    crab_positions = parse_data()

    # target_position = align_crabs(crab_positions)
    # spent_fuel = calculate_spent_fuel(crab_positions, target_position)

    target_position_1, target_position_2 = align_crabs_v2(crab_positions)
    spent_fuel_1 = calculate_spent_fuel_v2(crab_positions, target_position_1)
    spent_fuel_2 = calculate_spent_fuel_v2(crab_positions, target_position_2)
    spent_fuel = min(spent_fuel_1, spent_fuel_2)

    print("\nThe least fuel possible they must spend is:", spent_fuel)


def parse_data():
    '''Funcion to parse the input data of the challenge.'''
    input_file = input("\nInput file: ")
    data = open(input_file, 'r').read().split("\n")

    crab_positions = dict()
    for number in data[0].split(","):
        crab_positions.update({
            int(number):
            crab_positions.get(int(number), 0) + 1,
        })

    return crab_positions


def align_crabs(crab_positions):
    '''Function to align crabs using the least fuel possible.'''
    crab_positions_sorted = list()
    for position in range(max(crab_positions.keys()) + 1):
        crab_positions_sorted.extend([position] *
                                     crab_positions.get(position, 0))

    crabs = len(crab_positions_sorted)
    if crabs % 2 == 0:
        median_position = (crab_positions_sorted[(crabs // 2) - 1] +
                           crab_positions_sorted[crabs // 2]) // 2
    else:
        median_position = crab_positions_sorted[crabs // 2]

    return median_position


def calculate_spent_fuel(crab_positions, target_position):
    '''Function to calculate the fuel spent by every crab.'''
    spent_fuel = 0
    for position, crabs in crab_positions.items():
        spent_fuel += abs(target_position - position) * crabs

    return spent_fuel


def align_crabs_v2(crabs_positions):
    '''Function to align crabs using the least fuel possible.'''
    crab_positions_sorted = list()
    for position in range(max(crabs_positions.keys()) + 1):
        crab_positions_sorted.extend([position] *
                                     crabs_positions.get(position, 0))

    mean_position = sum(crab_positions_sorted) / len(crab_positions_sorted)
    return math.ceil(mean_position), math.floor(mean_position)


def calculate_spent_fuel_v2(crab_positions, target_position):
    '''Function to calculate the fuel spent by every crab.'''
    spent_fuel = 0
    for position, crabs in crab_positions.items():
        spent_fuel += sum(range(abs(target_position - position) + 1)) * crabs

    return spent_fuel


if __name__ == "__main__":
    main()
