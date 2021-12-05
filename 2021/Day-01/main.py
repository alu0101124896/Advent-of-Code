'''
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2021
Description: This program implemets my solution to the Advent of Code challenge.
'''


def main():
    '''Main function to resolve the challenge.'''
    depth_reports = parse_data()

    result = num_of_depth_increases(depth_reports)

    print("\nThe number of measurements that are larger than the previous is:",
          result)


def parse_data():
    '''Funcion to parse the input data of the challenge.'''
    input_file = input("\nInput file: ")
    data = open(input_file, 'r').read().split("\n")

    if data[len(data) - 1] == '':
        data.pop()

    return [int(number) for number in data]


def num_of_depth_increases(depth_reports):
    '''Function to calculate the number of times a depth measurement increases
     from the previous measurement.'''
    return len([
        1 for index, depth in enumerate(depth_reports[:-1])
        if depth < depth_reports[index + 1]
    ])


if __name__ == "__main__":
    main()
