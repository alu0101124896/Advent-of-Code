'''
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2021
Description: This program implemets my solution to the Advent of Code challenge.
'''


def main():
    '''Main function to resolve the challenge.'''
    octopuses_energy = parse_data()

    octopus_flashes = count_flashes(octopuses_energy)

    print("\nThe number of total flashes in 100 steps is:", octopus_flashes)


def parse_data():
    '''Funcion to parse the input data of the challenge.'''
    input_file = input("\nInput file: ")
    data = open(input_file, 'r').read().split("\n")

    if data[len(data) - 1] == '':
        data.pop()

    return [[int(number) for number in line] for line in data]


def count_flashes(octopuses_energy):
    '''Function to count the number of flashes after 100 steps.'''
    flashes = 0
    for _ in range(100):
        has_not_flashed = [[True for octopus in line] for line in octopuses_energy]
        octopuses_energy = [[octopus_energy + 1 for octopus_energy in line]
                            for line in octopuses_energy]

        while True:
            prev_state = [line.copy() for line in octopuses_energy]

            for line_index, line in enumerate(octopuses_energy):
                for octopus_index, octopus_energy in enumerate(line):
                    if (octopus_energy > 9
                            and has_not_flashed[line_index][octopus_index]):
                        increment_nearby(line_index, octopus_index,
                                         octopuses_energy)
                        has_not_flashed[line_index][octopus_index] = False

            if octopuses_energy == prev_state:
                break

        octopuses_energy = [[
            0 if octopus_energy > 9 else octopus_energy
            for octopus_energy in line
        ] for line in octopuses_energy]

        flashes += sum([
            octopus_energy == 0 for line in octopuses_energy
            for octopus_energy in line
        ])

    return flashes


def increment_nearby(line_index, octopus_energy_index, octopuses_energy):
    '''Function to increment in one the energy of the neaby octopuses.'''
    if line_index - 1 >= 0:
        if octopus_energy_index - 1 >= 0:
            octopuses_energy[line_index - 1][octopus_energy_index - 1] += 1
        octopuses_energy[line_index - 1][octopus_energy_index] += 1
        if octopus_energy_index + 1 < len(octopuses_energy[line_index - 1]):
            octopuses_energy[line_index - 1][octopus_energy_index + 1] += 1

    if octopus_energy_index - 1 >= 0:
        octopuses_energy[line_index][octopus_energy_index - 1] += 1
    if octopus_energy_index + 1 < len(octopuses_energy[line_index]):
        octopuses_energy[line_index][octopus_energy_index + 1] += 1

    if line_index + 1 < len(octopuses_energy):
        if octopus_energy_index - 1 >= 0:
            octopuses_energy[line_index + 1][octopus_energy_index - 1] += 1
        octopuses_energy[line_index + 1][octopus_energy_index] += 1
        if octopus_energy_index + 1 < len(octopuses_energy[line_index + 1]):
            octopuses_energy[line_index + 1][octopus_energy_index + 1] += 1


if __name__ == "__main__":
    main()
