'''
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2021
Description: This program implemets my solution to the Advent of Code challenge.
'''


def main():
    '''Main function to resolve the challenge.'''
    scanner_reports = parse_data()

    print("\nThe ... is:", scanner_reports)


def parse_data():
    '''Funcion to parse the input data of the challenge.'''
    # input_file = input("\nInput file: ")
    input_file = "./2021/Day-19/test.txt"
    data = open(input_file, 'r', encoding="utf-8").read().split("\n\n")

    scanner_reports = list()
    for line in data:
        line = line.split("\n")[1:]
        if line[-1] == '':
            line.pop()
        scanner_reports.append(
            [[int(position) for position in beacons.split(',')]
             for beacons in line])

    return scanner_reports


if __name__ == "__main__":
    main()
