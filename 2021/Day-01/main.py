'''
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2021
Description: This program implemets my solution to the Advent of Code challenge.
'''


def main():
    '''Main function to resolve the challenge.'''
    depth_reports = parse_data()

    # result = num_of_depth_increases(depth_reports)
    result = num_of_depth_increases(depth_reports, sliding_window=3)

    # print("\nThe number of measurements that are larger than the previous is:",
    #       result)
    print("\nThe number of sums that are larger than the previous is:", result)


def parse_data():
    '''Funcion to parse the input data of the challenge.'''
    input_file = input("\nInput file: ")
    data = open(input_file, 'r').read().split("\n")

    if data[len(data) - 1] == '':
        data.pop()

    return [int(number) for number in data]


def num_of_depth_increases(depth_reports, sliding_window=1):
    '''Function to calculate the number of times a depth measurement increases
    from the previous measurement.
    '''
    return len([
        1 for index, _ in enumerate(depth_reports[:-sliding_window])
        if sum(depth_reports[index:(index + sliding_window)]) <
            sum(depth_reports[(index + 1):(index + sliding_window + 1)])
    ])


if __name__ == "__main__":
    main()
