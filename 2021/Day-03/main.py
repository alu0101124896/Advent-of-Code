'''
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2021
Description: This program implemets my solution to the Advent of Code challenge.
'''


def main():
    '''Main function to resolve the challenge.'''
    diagnostic_report = parse_data()

    power = power_consumption(diagnostic_report)

    print("\nThe power consumption of the submarine is:", power)


def parse_data():
    '''Funcion to parse the input data of the challenge.'''
    input_file = input("\nInput file: ")
    data = open(input_file, 'r').read().split("\n")

    if data[len(data) - 1] == '':
        data.pop()

    return [[int(digit) for digit in binary_number] for binary_number in data]


def power_consumption(diagnostic_report):
    '''Function to calculate the power consumption of the submarine.'''
    diagnostic_report_t = list(zip(*diagnostic_report))

    gamma_rate = ""
    epsilon_rate = ""
    for row in diagnostic_report_t:
        if sum(row) < len(row) / 2:
            gamma_rate += "0"
            epsilon_rate += "1"
        else:
            gamma_rate += "1"
            epsilon_rate += "0"

    gamma_rate = int(gamma_rate, 2)
    epsilon_rate = int(epsilon_rate, 2)

    return gamma_rate * epsilon_rate


if __name__ == "__main__":
    main()
